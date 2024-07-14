
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from cusum import Cusum_cal


csv_path = './mh/mental_disorder.csv'
df = pd.read_csv(csv_path)
country_names = set(df['location_name'].to_numpy())


def main(country_name) -> None:

    print(f"location_name == \"{country_name}\" and metric_name == \'Rate\'")
    df_c = df.query(f"location_name == \'{country_name}\' and metric_name == \'Rate\'")[
        ['year', 'val', 'upper', 'lower']].copy(deep=True)

    vals = df_c['val'].to_numpy()
    vals = vals/np.max(vals)
    # Standardized by diving by max vals

    vals_cusum = Cusum_cal(vals)
    df_vals = vals_cusum.compute(
        np.mean(vals[0:-2]), np.std(vals[0:-2]), w=1, output_original=True)

    df_c_y_v = (df_c[['year', 'val']].copy(deep=True)).reset_index()
    df_combined = df_c_y_v.join(df_vals)

    val_fig = df_c.plot(x='year')
    cusum_fig = df_vals.plot()
    country_name_out = country_name.replace(' ', "_").replace(chr(92), '')
    val_fig.get_figure().savefig(f'./output/{country_name_out}_md_values.png')
    cusum_fig.get_figure().savefig(f'./output/{country_name_out}_md_cusum.png')
    df_combined.to_csv(f'./output/{country_name_out}_md_cusum.csv')
    print(f'{country_name_out} is done.')
    plt.close()


for i in country_names:
    i = i.replace("'", "\\'")
    main(i)
