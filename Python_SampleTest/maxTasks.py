N = int(input("Number of problems:"))
P = int(input("Time to reach party:"))

total = 240
remaining = total - P

count = 0

for i in range(1, N+1):
    time_required = 5 * i
    if(remaining > time_required):
        count += 1
        remaining -= time_required
    else:
        break

print(count)