n = int(input("Enter the number of seats in a row:"))
arr = list(map(int, input().split()))
count = 0

for i in arr:
    if i == 0:
        count += 1
    else:
        continue

print(count)