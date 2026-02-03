class creditException(Exception):
    pass

class salaryException(Exception):
    pass

try:
    credit_score = int(input("Credit Score:"))
    salary = int(input("Salary:"))

    if credit_score < 700:
        raise creditException
    if salary < 25000:
        raise salaryException
    print("Loan Approved")
    
except creditException:
    print("Low Credit Score")

except salaryException:
    print("Low Salary")