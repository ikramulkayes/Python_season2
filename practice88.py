class Graduate_Student:
    number_of_graduate_students = 0

    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    def __str__(self):
        s =  "Department: "+self.name+", Course Credits: "+str(self.credits)
        return s
class MSc_Student(Graduate_Student):
    def __init__(self, name, credits):
        super().__init__(name, credits)
        self.lst = {}
    def add_MSc_Student(self,*args):
        count = len(args)
        for i in range(0,count+1,2):
            self.lst[args[i]] = args[i+1]
            Graduate_Student.number_of_graduate_students += 1
    def __str__(self):
       s= super().__str__() + "\n"
       for key,val in self.lst.items():
           s+= f"Name: {key}, Course Credits remaining: {val-self.credits}\n"
        return s.rstrip("\n")
        

    

# Write your codes here.
# Do not change the following lines of code.
p1 = MSc_Student("CSE", 18)
print("=================================")
p1.add_MSc_Student("Daniel", 12,  "Catherine", 18, "Michael", 15)
print("=================================")
print(p1)
print("=================================")
p2 = MEng_Student("CSE", 30)
print("=================================")
p2.add_MEng_Student("Barry", 12, "Sam", 18)
print("=================================")
print(p2)
print("=================================")
print("Total GraduateStudent: ", 
Graduate_Student.number_of_graduate_students)