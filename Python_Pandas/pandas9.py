import pandas as pd
import numpy as np

data = np.array(['a','b','c','d','e','f','g','h','i','i'])
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
print(ser[16])

# Error 