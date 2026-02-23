from abc import ABC, abstractmethod

class Dog(ABC):  # Abstract class
    def __init__(self, name):
        self.name = name

    @abstractmethod  
    def sound(self):  # Abstract method
        pass

    def display_name(self):  # Concrete method
        print("Dog's name:", self.name)

class Labrador(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador woofs!")

class Beagle(Dog):
    def sound(self):
        print("Beagle Bark!")

dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()
    dog.sound()