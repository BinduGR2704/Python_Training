N = int(input("Number of files:"))
arr = list(input())

max = 0

if N == 0:
    print(-1)

for s in arr:
    num = int(s[-1])
    if num > max:
        max = num

print(max)

# N = int(input("Number of files: "))
# arr = input().split()   # split into file names

# max_num = 0

# if N == 0:
#     print(-1)
# else:
#     for s in arr:
#         num = int(s.split("_")[-1]) 
#         if num > max_num:
#             max_num = num

#     print(max_num)

