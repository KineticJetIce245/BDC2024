import os
import pandas as pd
import numpy as np

path = './output/'
files = os.listdir(path)

remarkable_number = 0


def check_if_remarkable(csv_path):
    df = pd.read_csv(csv_path)
    sh_array = df['SH Array'].to_numpy()
    five_sigma = 5*np.std(sh_array[:-2])
    print(str(five_sigma) + " vs " +
          str(sh_array[-1]) + " or " + str(sh_array[-2]))
    if (five_sigma < sh_array[-1]) or (five_sigma < sh_array[-2]):
        return True
    else:
        print('stop')


number_of_countries = 0
for f in files:
    if (f.__contains__('csv')):
        print(f)
        if (check_if_remarkable(path + f)):
            remarkable_number += 1
        number_of_countries += 1

print('number of countries: ' + str(number_of_countries))
print('remarkable number: ' + str(remarkable_number))
print('percentage: ' + str(remarkable_number/number_of_countries*100) + '%')
