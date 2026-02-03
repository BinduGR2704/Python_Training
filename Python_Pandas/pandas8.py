import pandas as pd
import numpy as np

data = np.array(['a','b','c','d','e','f','g','h','i','i'])
ser = pd.Series(data)

print(ser[:5])