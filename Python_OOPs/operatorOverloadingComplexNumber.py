class ComplexNumber:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        real_sum = self.real + other.real
        img_sum = self.img + other.img
        return ComplexNumber(real_sum , img_sum)

    def __str__(self):
        return f"{self.real} + {self.img}i"
    
v1 = ComplexNumber(1, 2)
v2 = ComplexNumber(3, 4)
v3 = v1 + v2

print(v3)