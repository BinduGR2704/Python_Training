class Exceeds(Exception):
    pass

Available_ticket = 10

try:
    name = input("User Name:")
    tickets = int(input("Requested tickets:"))

    if tickets > Available_ticket:
        raise Exceeds
    if tickets <= 0:
        raise ValueError
    print("Booking Successful")
    print("Transaction Completed")
    Available_ticket -= tickets
    print("Available Seats:", Available_ticket)

except Exceeds:
    print("Requested tickets exceed available seats")

except ValueError:
    print("Invalid request")