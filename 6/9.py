class Student:
    total_student = 0
    brac_student = 0
    other_student = 0
    def __init__(self,name,dept,uni ="BRAC University" ):
        self.name = name
        self.dept = dept
        self.university = uni
        if self.university =="BRAC University":
            Student.brac_student += 1
        else:
            Student.other_student += 1
            
        Student.total_student += 1
    @classmethod
    def createStudent(cls,name,dept,uni="BRAC University"):
        obj = cls(name,dept,uni)
        
        return obj
    @classmethod
    def printDetails(cls):
        print("Total Student(s):",Student.total_student)
        print("BRAC University Student(s):",Student.brac_student)
        print("Other Institution Student(s):",Student.other_student)
    def individualDetail(self):
        print("Name:",self.name)
        print("Department:",self.dept)
        print("Institution:",self.university)


Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
    
    