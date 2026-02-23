class Customer:
    def __init__(self, name, age, address, phone, aadhaar, pan):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.aadhaar = aadhaar
        self.pan = pan

    def display(self):
        print("\nPerson Details")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)
        print("Phone No: ", self.phone)
        print("Adhaar No: ", self.aadhaar)
        print("Pan No: ", self.pan)


name = input("Enter name: ")
age = int(input("Enter age: "))
address = input("Enter address: ")
phone = input("Enter phone number: ")
aadhaar = input("Enter Aadhaar number: ")
pan = input("Enter PAN card number: ")

person = Customer(name, age, address, phone, aadhaar, pan)

person.display()
