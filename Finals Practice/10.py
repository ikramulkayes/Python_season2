class Graduate_Student:
    number_of_graduate_students = 0

    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    def __str__(self):
        s =  "Department: "+self.name+", Course Credits: "+str(self.credits)
        return s

# Write your codes here.
class MSc_Student(Graduate_Student):
    mscstudents = 0
    def __init__(self, name, credits):
        super().__init__(name, credits)
        self.dic = {}
        print(f"MSc Students in CSE have to complete {self.credits} hours for courses.")
    def add_MSc_Student(self,*args):
        count = 0
        for elm in range(0,len(args),2):
            self.dic[args[elm]] = args[elm+1]
            MSc_Student.mscstudents += 1
            Graduate_Student.number_of_graduate_students +=1
    def __str__(self):
        print( super().__str__())
        print(f"Total Student(s):{MSc_Student.mscstudents}")
        print("Total Student(s):")
        s = ""
        for k,v in self.dic.items():
            s+= f"Name: {k}, Course Credits remaining: {self.credits-v}\n"
        s = s.rstrip("\n")
        return s

class MEng_Student(Graduate_Student):
    mscstudents = 0
    def __init__(self, name, credits):
        super().__init__(name, credits)
        self.dic = {}
        print(f"MEng Students in CSE have to complete {self.credits} hours for courses.")
    def add_MEng_Student(self,*args):
        count = 0
        for elm in range(0,len(args),2):
            self.dic[args[elm]] = args[elm+1]
            MEng_Student.mscstudents += 1
            Graduate_Student.number_of_graduate_students +=1
    def __str__(self):
        print( super().__str__())
        print(f"Total Student(s):{MEng_Student.mscstudents}")
        print("Total Student(s):")
        s = ""
        for k,v in self.dic.items():
            s+= f"Name: {k}, Course Credits remaining: {self.credits-v}\n"
        s = s.rstrip("\n")
        return s          







#Do not change the following lines of code.

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