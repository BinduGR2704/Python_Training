f = open("abstraction.py", "r")
line = f.readline()
while line:
    print(line.strip())
    line = f.readline()

f.close()