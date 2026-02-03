n = int(input("Enter the number of people:"))
c = int(input("Enter ship capacity:"))

count = 0

while(n > 0):
    n = n - c
    count += 1

print(count)