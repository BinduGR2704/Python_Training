pwd = "admin"

try:
    username = input("Username:")
    password = input("Password:")
    balance = input("Balance Amount:")
    withdraw = input("Withdrawal Amount:")

    if password != pwd:
        raise ValueError
    if balance < withdraw:
        print("Insufficient Balance")
    else:
        print("Transaction successful")

except ValueError:
    print("Authentication Failed")

finally:
    print("Session closed")
    