class Student:

    def __init__(self):
        self.__name = "ABCD"
        self.__age = 21
        self.__sub1 = ""
        self.__sub2 = ""
        self.__sub3 = "" 
        self.__sub4 = ""
        self.__sub5 = ""
        self.__physics = 00
        self.__chemistry = 00
        self.__maths = 00
        self.__java = 00
        self.__OS = 00
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_marks(self):
        # return self.__physics, self.__chemistry, self.__maths, self.__java, self.__OS
        print("Physics:",self.__physics)
        print("Chemistry:", self.__chemistry)
        print("Maths:", self.__maths)
        print("Java:", self.__java)
        print("OS:", self.__os)
    
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_subject(self, sub1, sub2, sub3, sub4, sub5):
        self.__sub1 = sub1
        self.__sub2 = sub2
        self.__sub3 = sub3
        self.__sub4 = sub4
        self.__sub5 = sub5

    def set_marks(self, physics, chemistry, maths, java, OS):
        self.__physics = physics
        self.__chemistry = chemistry
        self.__maths = maths
        self.__java = java
        self.__os = OS

person = Student()
person.set_name("Peter")
person.set_age(23)
person.set_subject("Physics", "Chemistry", "Maths", "Java", "OS")
person.set_marks(99, 98, 96, 90, 85)
print(person.get_name())
print(person.get_age())
person.get_marks()