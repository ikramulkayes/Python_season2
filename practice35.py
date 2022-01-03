class Student:
    def __init__(self,name):
        self.name = name
        self.id = None
    def change_name(self,name=None):
        self.name = name
    def get_name(self):
        return self.name





student = Student("Hossain")
student.change_name("Hussain")
student.change_name()
print(student.get_name())




class A:
    def __init__(self,value):
        self.value = value
    def change_value(self,value):
        self.value = value
        return 0

a = A(10)
print(a.value,end=" ")
b = A(20)
print(b.value, a.change_value(b.value))