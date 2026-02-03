import numpy as np

x = np.array([1,2,3])
y = np.array([4,5,6])

print(x+y) # OR np.add(x, y)
print(x-y) # OR np.subtract(x, y)
print(x*y) # OR np.multiply(x, y)
print(x/y) # OR np.divide(x, y)

a = np.array([-3, 1, 2, -4, 3, 4])
print(np.absolute(a))