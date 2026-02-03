import numpy as np

a1 = np.eye(3)
a2 = np.diag([1,2,3])
a3 = np.zeros_like(a2)
a4 = np.ones_like(a2)

print(a1)
print(a2)
print(a3)
print(a4)