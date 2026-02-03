s1 = input("Enter string 1:")
s2 = input("Enter string 2:")

n = len(s1)
m = len(s2)

dp = [[0] * (m+1) for _ in range(n+1)]

max_len = 0
end_index = 0  

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

            if dp[i][j] > max_len:
                max_len = dp[i][j]
                end_index = i
        else:
            dp[i][j] = 0

if max_len == 0:
    print(0)

lcs = s1[end_index - max_len: end_index]

ascii_sum = 0
for ch in lcs:
    ascii_sum += ord(ch)

print(ascii_sum)