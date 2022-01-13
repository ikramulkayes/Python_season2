class Student:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit

    def __str__(self):
        s = f"Name: {self.name}\nCredit completed: {self.credit}"
        return s

# Write your codes here.
class MNSStudent(Student):
    def __init__(self, name, credit,id):
        super().__init__(name, credit)
        self.id = id
        self.dic = {}
        self.ccount = 0
    def addCourses(self,*args):
        for elm in args:
            k = elm[3::]
            k = k[0] + "00"
            if k not in self.dic.keys():
                self.dic[k] = [elm]
            else:
                temp = self.dic[k]
                temp.append(elm)
                self.dic[k] = temp
            self.ccount += 1
    def showTuitionFee(self):
        print(f"{self.name}, your tuition fee is {self.ccount*18900}")
    def __str__(self):
        print(super().__str__())
        s = f"ID: {self.id}\n"
        s+= "Course Details:\n"
        for k,v in self.dic.items():
            s+=f"{k} Level: {v}\n"
        s = s.rstrip("\n")
        return s
class EEEStudent(MNSStudent):
    def __init__(self, name, credit, id):
        super().__init__(name, credit, id)


        
# Do not change the following lines of code.
s1 = MNSStudent("David", 56, 21336007)
s1.addCourses("PHY201","PHY112","PHY270","MAT110","CSE330")
print('====================================')
s1.showTuitionFee()
print('====================================')
print(s1)
print('====================================')
s2 = EEEStudent("Mike", 32, 21321168)
s2.addCourses("CSE110", "EEE201", "EEE480", "EEE449")
print('====================================')
s2.showTuitionFee()
print('====================================')
print(s2)