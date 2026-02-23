class Employee:
    
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

class SalesEmployee(Employee):

    def __init__(self, id, salary, sales):
        super().__init__(id, salary)
        self.sales = sales

    def get_details(self):
        print("id:", self.id)
        print("Salary:", self.salary)
        print("Sales:", self.sales)

id = int(input("Enter the ID:"))
salary = int(input("Enter the salary:"))
sales = int(input("Enter the sales:"))
emp1 = SalesEmployee(id, salary, sales)
emp1.get_details()