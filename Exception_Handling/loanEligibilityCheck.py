try:
    salary = int(input("Enter the salary:"))
    if salary < 20000:
        raise ValueError
    print("Loan Approved")
except ValueError:
    print("Loan Rejected")