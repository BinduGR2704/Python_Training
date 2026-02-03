marks = input("Enter the marks: ")

try:
    mark = int(marks)
    if mark > 0 and mark < 100:
        print("Valid marks")
    else:
        print("Invalid marks")

except ValueError:
    print("Invalid marks")

# try:
#     marks = input()

#     if marks < 0 or marks > 100:
#         raise ValueError
    
#     print("Valid marks")

# except ValueError:
#     print("Invalid marks")