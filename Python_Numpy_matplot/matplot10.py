import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apples','Bananas','Cherries','Dates']
sales = [400,350,300,450]

plt.bar(fruits,sales, color='violet')  # OR plt.brah - means plot horizontal bars
plt.title('Fruit Sales')
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.show()