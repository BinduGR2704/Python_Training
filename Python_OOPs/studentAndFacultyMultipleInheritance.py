class Student:

    def __init__(self, sid, deptid):
        self.sid = sid
        self.deptid = deptid

    def get_info(self):
        print("Student ID:", self.sid)
        print("Department ID:", self.deptid) 

class Faculty:

    def __init__(self, eid, deptid):
        self.eid = eid
        self.deptid = deptid

    def get_info(self):
        print("Employee ID:", self.eid)
        print("Department ID:", self.deptid)

class phDStudent(Student, Faculty):

    def __init__(self, sid, eid, deptid):
        Student.__init__(self, sid, deptid)
        Faculty.__init__(self, eid, deptid)

    def get_info(self):
        print("Student ID:", self.sid)
        print("Employee ID:", self.eid)
        print("Department ID:", self.deptid)

sid = int(input("Enter the student id:"))
eid = int(input("Enter Employee id:"))
deptid = int(input("Enter Department id:"))

phDstud1 = phDStudent(sid, eid, deptid)
phDstud1.get_info()
