class Vaccine:
    def __init__(self,name,country,days):
        self.vname = name
        self.days = days
        

class Person:
    def __init__(self,name,age,prof = "General Citizen"):
        self.name = name
        self.age = age
        self.prof = prof
        self.dic = {"1st dose":None, "2nd dose":None}
        self.flag = True
        self.fv = None
        self.daysleft = None
    def pushVaccine(self,gg,dose = "1st dose"):
        dose = dose.lower()
        if self.flag:
            self.fv = gg.vname
            self.daysleft = gg.days
            self.flag = False
        if self.fv == gg.vname:
            if self.prof == "Student":
                print(f"{dose} done for {self.name}")
                self.dic[dose] = "Given"
            else:
                if self.age >=25:
                    print(f"{dose} done for {self.name}")
                    self.dic[dose] = "Given"
                else:
                    print(f"Sorry {self.name}, Minimum age for taking vaccines is 25 years now.")
        else:
            print(f"Sorry {self.name}, you can’t take 2 different vaccines")
    def showDetail(self):
        print("Name:",self.name,"Age:",self.age,"Type:",self.prof)
        print("Vaccine name:",self.fv)
        for k,v in self.dic.items():
            if v == "Given":
                print(k+": "+v)
            else:
                print(f"{k}: Please come after {self.daysleft} days")


astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")



        
