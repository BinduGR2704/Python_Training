from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod  # @ is a decorator, is a function that modifies or extends the behavior of another function without changing its code.
    def say_hello(self):
        pass  # Abstract method 

class English(Greet):
    def say_hello(self):
        return "Hello!"
        
g = English()
print(g.say_hello())   