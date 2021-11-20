class Student:
    def __init__(self,name=None,dept=None):
        if name == None and dept == None:
            print("Student name and department need to be set")
        elif dept == None:
            print(f"Department for {name} needs to be set")
        else:
            print(f"{name} is from {dept} department")
        self.name = name
        self.dept = dept
        self.lst = []
        self.final = ""
    def update_name(self,name):
        self.name = name
    def update_department(self,name):
        self.dept = name
    def enroll(self,*args):
        for elm in args:
            self.lst.append(elm)
            self.final += elm +", "
        self.final = self.final.rstrip(", ")
    def printDetail(self):
        print("Name:",self.name)
        print("Department:",self.dept)
        print(f"{self.name} enrolled in {len(self.lst)} course(s)")
        print(self.final)

    

s1 = Student()
print('=========================')
s2 = Student('Carol')
print('=========================')
s3 = Student('Jon', 'EEE')
print('=========================')
s1.update_name('Bob')
s1.update_department('CSE')
s2.update_department('BBA')
s1.enroll('CSE110', 'MAT110', 'ENG091')
s2.enroll('BUS101')
s3.enroll('MAT110', 'PHY111')
print('###########################')
s1.printDetail()
print('=========================')
s2.printDetail()
print('=========================')
s3.printDetail()