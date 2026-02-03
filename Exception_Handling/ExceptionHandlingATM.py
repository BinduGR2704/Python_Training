balance = 60000

withdraw_amount = input("Enter the amount to be withdrawn:")

try:
    amount = int(withdraw_amount)
    if amount < balance:
        print("Withdraw successful")
    else:
        print("Insuffient balance")

except ValueError:
    print("Invalid amount")

# try:
#     balance = int(input("Enter balance amount:"))
#     withdraw = int(input("Enter withdraw amount:"))
#     if withdraw > balance:
#         print("Insufficient balance")
#     else:
#         print("Withdraw successful")
# except ValueError:
#     print("Invalid data")