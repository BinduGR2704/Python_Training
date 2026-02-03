N = int(input("Enter total communities:"))
arr = list(map(int, input().split()))

prod = 1

for i in arr:
    if i % 7 == 0:
        prod *= i
else:
    prod = 0

print(prod)