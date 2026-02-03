class A:
    def operate(self, a, b):
        return a + b
    
class B:
    def operate(self, str):
        return str
    
a = A()
print(a.operate(10, 20))
b = B()
print(b.operate("Hello"))