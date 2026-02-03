import matplotlib.pyplot as plt
import seaborn as sns

x = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
y = [5,6.7,4,6,2,4.9,1.8]

ax = sns.stripplot(x=x, y=y)
ax.set(xlabel='Days', ylabel='Amount spent')
plt.title("Daily spending")
plt.show()