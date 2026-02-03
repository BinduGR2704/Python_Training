N = int(input("Number of team members:"))
s = list(input().split())

initials = ""

for s1 in s:
    initials += (s1[0])

print(initials)