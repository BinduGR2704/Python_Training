N = int(input("Enter the number of rooms occupied:"))
arr = list(map(int, input().split()))
T = int(input("Enter the total number of rooms:"))

vacancy = T - N

print(vacancy)