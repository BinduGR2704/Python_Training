class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Dog's name:",self.name)

class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador):
    def Guide(self):
        print(self.name ,"Guides the way")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!!")

class GoldenRetriever(Dog, Friendly):
    def sound(self):
        print("Golden Retriever Barks")

lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.Guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()