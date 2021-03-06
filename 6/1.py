class Student:
    id = 0
    def __init__(self,name,department,age,cgpa):
        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa
        Student.id += 1
    def get_details(self):
        print("ID:",Student.id)
        print("Name:",self.name)
        print("Department:",self.department)
        print("Age:",self.age)
        print("CGPA:",self.cgpa)
    @classmethod
    def from_String(cls,word):
        name,dept,age,cgpa = word.split("-")
        obj = cls(name,dept,age,cgpa)
        return obj

s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()


# Write the answer of subtask 5 here
#class variable refers to class itself and instance variable refers to the object

# Write the answer of subtask 6 here
#we can use class variable and work with class in class methods and in instance method we have self method which lets us work with the object created by the class
