
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# |%%--%%| <JrVduAWhra|QaNRgqRH>

df_covid = pd.read_csv('owid-covid-data.csv')
df_mental = pd.read_csv('IHME-GBD_2021_DATA-31d34781-1.csv')

# |%%--%%| <QaNRgqRH|h8dAbYFzZ1>

df_covid.columns

# |%%--%%| <h8dAbYFzZ1|M9kFeRkhlG>

df_mental.columns

# |%%--%%| <M9kFeRkhlG|5CMFBXL1hM>

usa_c = (df_covid[df_covid['iso_code'] == 'USA'])
usa_c

|%%--%%| <5CMFBXL1hM|tfMNA0MwM3>

usa_c_20 = usa_c.query("date.str.contains('2020')")
usa_c_20[['new_cases']].sum(0, numeric_only = True)
usa_c_20[['new_cases']].mean(0, numeric_only = True)

#|%%--%%| <tfMNA0MwM3|4jr0Xjxg9x>


