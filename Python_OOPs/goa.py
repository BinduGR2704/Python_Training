class Goa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def drinking(self):
        print(self.name, "is drinking water")

    def beach(self):
        print(self.name, "is in beach")

    def temple(self):
        print(self.name, "is visiting a temple")

    def boating(self):
        print(self.name, "is boating")

    def resort(self):
        print(self.name, "is having fun at resort")

print("Welcome to Goa!! Please enter your details here")
name = input("Name: ")
age = int(input("Age: "))

person = Goa(name, age)
list = [person.drinking(), person.beach(), person.temple(), person.boating(), person.resort()]

for i in list:
    i