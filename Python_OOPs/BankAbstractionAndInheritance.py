from abc import ABC, abstractmethod
class Bank(ABC):

    def __init__(self, p, t, r):
        self.p = p
        self.t = t
        self.r = r

    @abstractmethod
    def Interest(self):
        pass

class canara(Bank):

    def __init__(self, p, t, r):
        super().__init__(p,t,r)

    def Interest(self):
        return (self.p*self.t*self.r)/100
    
class SBI(Bank):

    def __init__(self, p, t, r):
        super().__init__(p,t,r)

    def Interest(self):
        return (self.p*self.t*self.r)/100 + 1
    
interest = canara(10000, 2, 0.08)
print(interest.Interest())
interest2 = SBI(20000, 1, 0.09)
print(interest2.Interest())