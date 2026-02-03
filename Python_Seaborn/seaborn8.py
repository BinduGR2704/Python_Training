import matplotlib.pyplot as plt
import seaborn as sn

plt.plot([0,1], [10,11], label='Line 1')
plt.plot([0,1], [11,10], label="Line 2")
plt.scatter([0,1], [10.5, 10.5], color='blue', marker='o', label='Dots')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line and Dot Plot")
plt.legend()
plt.show()