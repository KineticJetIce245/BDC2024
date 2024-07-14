import os
import pandas as pd
import numpy as np

path = './output/'
files = os.listdir(path)

remarkable_number = 0


def check_if_remarkable(csv_path):
    df = pd.read_csv(csv_path)
    print("Standard deviation: " + str(np.std(df['Received Array'])))
    max_SH = np.max(df['SH Array'])
    print('last' + str(df['SH Array']))
    if (np.max(df['SH Array']) > 10):
        return True


number_of_countries = 0
for f in files:
    if (f.__contains__('csv')):
        print(f)
        if (check_if_remarkable(path + f)):
            remarkable_number += 1
        number_of_countries += 1

print('number of countries: ' + str(number_of_countries))
print('remarkable number: ' + str(remarkable_number))
