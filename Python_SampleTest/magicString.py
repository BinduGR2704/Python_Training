s = input("Enter the string:")

char_set = set(s)

freq = 0

for i in char_set:
    count = s.count(i)
    if count > freq:
        freq = count

length = len(s)

print(length-count)