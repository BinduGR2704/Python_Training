class Animal:
    def sound(self):
        return "Some generic sound"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(Self):
        return "Meow"
    
animal = [Animal(), Dog(), Cat()]
for i in range(0, 3):
    print(animal[i].sound())