N = int(input("Total number of voters:"))
arr = list(map(int, input().split()))
unique = set(arr)
freq = 0
win = 0

for value in unique:
    count = arr.count(value)

    if count > freq:
        freq = count
        win = value

if freq >= N / 2:
    print(win)
else:
    print(-1)