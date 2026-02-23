class Employee:
    def __init__(self):
        self.__salary = 50000

    def get_salary(self):  # Getter method
        return self.__salary
    
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Inavild salary amount")

emp = Employee()
print(emp.get_salary())

emp.set_salary(60000)
print(emp.get_salary())