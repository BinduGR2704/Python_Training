a = input("Enter a: ")
b = input("Enter b: ")

try:
    a1 = int(a)
    b1 = int(b)
    res = a1 / b1
    print("Result:", res)

except ValueError:
    print("Enter valid inputs")

except ZeroDivisionError:
    print("Cannot be divided by zero!! Enter valid inputs")

# try:
#     a = 10
#     b = 20
#     res = a/b
#     print("Result:", res)
# except ZeroDivisionError:
#     print("Cannot be divided by zero")
# except ValueError:
#     print("Give valid inputs")