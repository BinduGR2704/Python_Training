try:
    withdraw = int(input("Enter the amount:"))
    if withdraw > 25000:
        raise ValueError
    print("Withdrawal Allowed")
except ValueError:
    print("Daily limit exceeded")