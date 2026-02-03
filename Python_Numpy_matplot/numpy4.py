import numpy as np

a = np.array([10,20,30,40,50])
idx = np.array([1,2,3])

print(a[idx])

cond = a > 30
print(a[cond])