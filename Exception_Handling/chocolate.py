import sys

N, K = map(int, sys.stdin.readline().split())

T = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))

max_type = max(T)

min_price = [float('inf')]*(max_type+1)

for i in range(N):
    if P[i] < min_price[T[i]]:
        min_price[T[i]] = P[i]

prices = []
for i in range(1, max_type + 1):
    if min_price[i] != float('inf'):
        prices.append(min_price[i])

if len(prices) < K:
    print("-1")
    sys.exit()

prices.sort()
total = sum(prices)

print(total)