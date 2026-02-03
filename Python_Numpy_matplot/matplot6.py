import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
temp = [22, 24, 23, 26, 25]

plt.plot(days, temp, marker='*')
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature(c)")
plt.show()