f = open("abstraction.py", "r")

for line in f:
    print(line.strip())

f.close()

# Open file in read mode
# Read the file line by line
# Close the file
# If "with" keyword is used while opening the file, it closes file automatically, no need to close the file manually.