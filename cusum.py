import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Cusum_cal :
    def __init__(self, array: np.array, w = 0.5) -> None:
        self.original_array = array
        self.__w_value = w
    
    def set_w(self, w_value) -> None:
        self.__w_value = w_value
    
    def compute(self, expect_mean, expect_std, w = 0.5) -> pd.DataFrame:
        df = {'Original Array' : self.original_array}
        
        z_array = []
        for i in range(len(self.original_array)):
            z_array.append((self.original_array[i]-expect_mean)/expect_std)
        
        df.update({'Z Array' : z_array})
        sH_array = [0]
        sL_array = [0]
        for i in range(len(self.original_array)-1):
            next_sH = sH_array[i] + z_array[i+1] - w
            next_sL = sL_array[i] - z_array[i+1] - w
            sH_array.append(next_sH if next_sH > 0 else 0)
            sL_array.append(next_sL if next_sL > 0 else 0)
             
        df.update({'SH Array' : sH_array})
        df.update({'SL Array' : sL_array})
        return pd.DataFrame(data=df)
    
    def standardize(self) -> np.array:
        o_array = self.original_array.copy()
        mean = np.mean(o_array)
        for i in range(len(o_array)):
            o_array[i] = o_array[i] - mean
        
        o_std = np.std(o_array)
        for i in range(len(o_array)):
            o_array[i] = o_array[i]/(o_std/0.5)
        
        return o_array

x = Cusum_cal([-0.60207, -0.85543, 0.4084, 0.60292, 0.14554, -0.11812, -0.22425, -0.25985, -0.26579, 0.70213, 0.32766, 0.55666, 0.50528, 0.62256, 0.21262, 0.36577, 0.85273, 1.0159, 0.53494, 1.4023])
df = x.compute(0, 0.5, 0.5)
print(df)
df.plot()
plt.show()
