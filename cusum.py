import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Cusum_cal:
    def __init__(self, array: np.array, w=0.5) -> None:
        self.original_array = array
        self.__w_value = w

    def set_w(self, w_value) -> None:
        self.__w_value = w_value

    def compute(self, expect_mean, expect_std, w=0.5, output_original=False) -> pd.DataFrame:
        df = {'Received Array': self.original_array} if output_original else {}

        z_array = []
        for i in range(len(self.original_array)):
            z_array.append((self.original_array[i]-expect_mean)/expect_std)

        df.update({'Z Array': z_array})
        sH_array = [0]
        sL_array = [0]
        for i in range(len(self.original_array)-1):
            next_sH = sH_array[i] + z_array[i+1] - w
            next_sL = sL_array[i] - z_array[i+1] - w
            sH_array.append(next_sH if next_sH > 0 else 0)
            sL_array.append(next_sL if next_sL > 0 else 0)

        df.update({'SH Array': sH_array})
        df.update({'SL Array': sL_array})
        return pd.DataFrame(data=df)
