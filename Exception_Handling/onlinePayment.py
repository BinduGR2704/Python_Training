try:
    card_number = input("Enter card number:")
    balance = input("Balance Amount:")
    withdraw = input("Withdrawal Amount:")

    if len(card_number) == 12:
        if balance > withdraw:
            print("Payment Successful")
        else:
            print("Payment Failed")
    else:
        raise ValueError
    
except ValueError:
    print("Invalid Card")