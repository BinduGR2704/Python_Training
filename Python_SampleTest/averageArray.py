N = int(input("Array size:"))
arr = list(map(int, input().split()))
sum = 0

arr.sort()

max1 = arr[-1]
max2 = arr[-2]

avg = (max1 + max2) / 2

for i in arr:
    if i >= avg:
        sum += i

print(sum)