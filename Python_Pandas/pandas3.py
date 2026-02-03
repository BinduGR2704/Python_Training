import pandas as pd

df = pd.read_csv("data-.csv")
print(df.head())  # Print first 5 rows

print(df.info())  # Information of columns/fields, their datatype etc

print(df.isnull().sum())  # Checks for null/empty values
df = df.fillna(0)         # Fills all the empty values with 0

ages = df[df['age']>25]
print(ages)               # Print rows whoes age is greater than 25

df['total'] = df['a'] + df['b']
print(df.head())                 # creates a new column to print total

res = df.groupby('category')['sales'].sum()
print(res)