def sum(a,b):
    x = a + b
    print(x)
def sum(a,b,c):
    x = a + b + c
    print(x)
#product(20,20)
class calculate:
    def square(self, a = None,b = None):
        if a!= None and b != None:
            return a* b
obj = calculate()
print("Square",obj.square())
print("square",obj.square(20))
print("Square",obj.square(30,30))



class stud:
    def __init__(self,ID,grd):
        self.ID = ID
        self.grade = grd
    def introduce(self):
        print("ID: ",ID, " Grade: ",self.grade)
stud1 = stud(101,"B")
stud1.age = 18
print(stud1,age)