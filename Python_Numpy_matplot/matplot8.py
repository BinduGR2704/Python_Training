import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = [3,6,9,12,15]
plt.plot(x,y, marker='o', linestyle='-', label='Data points')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plots")
plt.legend()
plt.show()