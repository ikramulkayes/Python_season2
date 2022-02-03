


class Student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def Details(self):
        return "Name: "+self.name+"\n"+"ID: "+self.ID+"\n"
#Write your code here
class CSEStudent(Student):
    def __init__(self, name, ID,sem):
        super().__init__(name, ID)
        self.sem = sem
        self.dic = {}
    def Details(self):
        k = super().Details()
        return k+ f"Current semester: {self.sem}"
    def addCourseWithMarks(self,*args):
        count = 0
        for elm in range(0,len(args),2):
            self.dic[args[count]] = args[count+1]
            count += 2
    def showGPA(self):
        print(f"{self.name} has taken {len(self.dic)} courses.")
        sum1 = 0
        cgpa = 0
        for k,v in self.dic.items():
            if v>=85:
                cgpa = 4.0
            elif v >= 80:
                cgpa = 3.3
            elif v >= 70:
                cgpa = 3.0
            elif v >=65:
                cgpa = 2.3
            elif v >= 57:
                cgpa = 2.0
            elif v >=55:
                cgpa = 1.3
            elif  v >= 50:
                cgpa = 1.0
            else:
                cgpa = 0.0
            sum1 += cgpa
            print(f"{k}: {cgpa}")
        print(f"GPA of {self.name} is : {round(sum1/len(self.dic),2)}")
    
            








Bob = CSEStudent("Bob","20301018","Fall 2020")
Carol = CSEStudent("Carol","16301814","Fall 2020")
Anny = CSEStudent("Anny","18201234","Fall 2020")
print("#########################")
print(Bob.Details())
print("#########################")
print(Carol.Details())
print("#########################")
print(Anny.Details())
print("#########################")
Bob.addCourseWithMarks("CSE111",83.5,"CSE230",73.0,"CSE260",92.5)
Carol.addCourseWithMarks("CSE470",62.5,"CSE422",69.0,"CSE460",76.5,"CSE461",87.0)
Anny.addCourseWithMarks("CSE340",45.5,"CSE321",95.0,"CSE370",91.0)
print("----------------------------")
Bob.showGPA()
print("----------------------------")
Carol.showGPA()
print("----------------------------")
Anny.showGPA()
