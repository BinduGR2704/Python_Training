try:
    age = int(input("Enter age:"))
    if age < 18 or age < 0:
        raise ValueError
    print("Valid age")

except ValueError:
    print("Invalid age")