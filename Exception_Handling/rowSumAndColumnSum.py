n = int(input("Enter matrix size: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

print("Row sum")
for row in matrix:
    sum = 0
    for j in range(n):
        sum += row[j]
    print(sum)

print("Column Sum")
for col in range(n):
    sum = 0
    for row in range(n):
        sum += matrix[row][col]
    print(sum)
