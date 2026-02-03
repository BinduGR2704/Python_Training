pin = 4123

try:
    pincode = int(input("Enter the PIN:"))
    if pincode != pin:
        raise ValueError
    print("Access Granted")

except ValueError:
    print("Invalid PIN")