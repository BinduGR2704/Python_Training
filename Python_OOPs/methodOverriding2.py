class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Bark!"
    
def make_animal_speak(animal):
    return animal.speak()

print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))