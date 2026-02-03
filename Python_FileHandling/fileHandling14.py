# try:
#     with open("balance.txt", "r", encoding="utf-8") as f:
#         balance = int(f.read().strip())

#     if balance != 0:
#         raise ValueError

#     print("Account closed")

# except ValueError:
#     print("Account has pending balance")

# except FileNotFoundError:
#     print("Balance file not found")

try:
    balance = int(input("Enter the balance amount:"))
    if balance != 0:
        raise ValueError
    print("Account closed")

except ValueError:
    print("Account has pending balance")