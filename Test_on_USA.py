
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#|%%--%%| <aJw7rL0s4Q|EqHeUc2gQi>

df_mental = pd.read_csv('IHME-GBD_2021_DATA-31d34781-1.csv')

#|%%--%%| <EqHeUc2gQi|ODBJV1Mp0V>

df_mental.columns

#|%%--%%| <ODBJV1Mp0V|52cYObfiR2>

df_USA = df_mental.query('location_name == \'United States of America\'')

#|%%--%%| <52cYObfiR2|VLnJg5UhXd>



#|%%--%%| <VLnJg5UhXd|egapPdK7U2
