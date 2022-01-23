class Student:
    total = 0
    csetotal = 0
    bbatotal = 0
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept
        self.temp = 0
        if self.dept =="CSE":
            Student.csetotal += 1
            self.temp = Student.csetotal

        else:
            Student.bbatotal += 1
            self.temp = Student.bbatotal
        Student.total += 1
        print(f"Creating Student Number: {Student.total}")
    def individualInfo(self):
        print(f"{self.name} is from {self.dept} department.")
        print(f"Serial of {self.name} among all students' is: {Student.total}")
        print(f"Serial of {self.name} in {self.dept} department is: {self.temp}")
    def totalInfo(self):
        print(f"Total Number of Student: {Student.total}")
        print(f"Total Number of CSE Student: {Student.csetotal}")
        print(f"Total Number of BBA Student: {Student.bbatotal}")




s1 = Student("Naruto", "CSE")
print('----------------------')
s1.individualInfo()
print('#############################')
s1.totalInfo()
print('============================')
 
s2 = Student("Sakura", "BBA")
print('----------------------')
s2.individualInfo()
print('#############################')
s2.totalInfo()
print('============================')
 
s3 = Student("Shikamaru", "CSE")
print('----------------------')
s3.individualInfo()
print('#############################')
s3.totalInfo()
print('============================')
 
s4 = Student("Deidara", "BBA")
print('----------------------')
s4.individualInfo()
print('#############################')
s4.totalInfo()
