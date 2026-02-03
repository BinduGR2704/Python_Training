f = open("abstraction.py", "r")
print("File Content")
print()
print(f.read())
print()
f.close()
print("File Closed")

# with open("abstraction.py", "r") as f: "with" will automatically close the file once block is executed
#     content = f.read()
#     print(content)  or print(f.read())

# This is file handling function where we open file in read mode and then print the content of the file and close the file.

# r - read
# w - write
# a - add/append
# t - create a text file
# b - create a binary file
# x - create specific file
# + - combine with other mode, Ex: "r+", "w+"
# encoding= - encode specific text
# newline= - move to new line
# wb , rb - write and read for binary(.bin) files [can be images, videos, binary data etc]
# syntax - open("file_name", "mode")