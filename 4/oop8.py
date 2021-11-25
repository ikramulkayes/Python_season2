class Student:
    def __init__(self,name,id,dept="CSE"):
        self.name = name
        self.id = id
        self.dept = dept
    def dailyEffort(self,time):
        self.hour = time
    def printDetails(self):
        if self.hour <=2:
            sug = 'Suggestion: Should give more effort!'
        elif self.hour <= 4:
            sug = "Suggestion: Keep up the good work!" 
        else:
            sug = 'Suggestion: Excellent! Now motivate others.'
        print("Name:",self.name)
        print("ID:",self.id)
        print("Department:",self.dept)
        print("Daily Effort:",self.hour,"hour(s)")
        print(sug)


harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()