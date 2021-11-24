class Student:
    def __init__(self,name = "default student"):
        self.name = name
    def quizcalc(self,*args):
        sum1 = 0
        for elm in args:
            sum1 += elm
        sum1 = sum1 / 3
        self.sum1 = sum1
    def printdetail(self):
        print(f"Hello {self.name}")
        print(f"Your average quiz score is {self.sum1}")
    

s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()



