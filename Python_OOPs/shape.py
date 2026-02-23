from abc import ABC, abstractmethod

class Shape(ABC):
    
    def __init__(self, c):
        self.color = c

    def get_color(self):
        return self.color
    
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self):
        return self.side * self.side
    
    def get_perimeter(self):
        return self.side * 4
    
s = Square("Red", 5.0)
print("Area:",s.get_area())
print("Perimeter:", s.get_perimeter())