class Developer:

    def __init__(self, eid1, deptid1):
        self.eid1 = eid1
        self.deptid1 = deptid1

    def get_info(self):
        print("Developer ID:", self.eid1)
        print("Department ID:", self.deptid1) 

class Designer:

    def __init__(self, eid2, deptid2):
        self.eid2 = eid2
        self.deptid2 = deptid2

    def get_info(self):
        print("Designer ID:", self.eid2)
        print("Department ID:", self.deptid2)

class phDStudent(Developer, Designer):

    def __init__(self, eid1, deptid1, eid2, deptid2):
        Developer.__init__(self, eid1, deptid1)
        Designer.__init__(self, eid2, deptid2)

    def get_info(self):
        print("Developer ID:", self.eid1)
        print("Department ID:", self.deptid1)
        print("Designer ID:", self.eid2)
        print("Department ID:", self.deptid2)

eid1 = int(input("Enter the Developer id:"))
deptid1 = int(input("Enter Department id:"))
eid2 = int(input("Enter Designer id:"))
deptid2 = int(input("Enter Department id:"))

phDstud1 = phDStudent(eid1, deptid1, eid2, deptid2)
phDstud1.get_info()
