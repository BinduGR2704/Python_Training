n = 10 
try:
   # n = int(abc) gives a value error
    res = n / 2 # or n/0 gives zero division error
except ZeroDivisionError:
    print("Cannot be divided by zero")
except ValueError:
    print("Enter a valid number")
else:
    print(res)
finally:
    print("Execution completed")

# a = ["10", "Hello", "20"]
# try:
#     total = int(a[0] + a[1])
# except (ValueError, TypeError) as e:
#     print("Error:", e)
# except IndexError:
#     print("Index error")