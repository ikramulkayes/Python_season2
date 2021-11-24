class Programmer:
    def __init__(self,name,language,exp):
        self.name = name
        self.language = language
        self.exp = exp
        print("Horray! A new programmer is born")
    def addExp(self,year):
        self.exp+= year
        print("Updating experience of",self.name)
    def printDetails(self):
        print("Name:",self.name)
        print("Language:",self.language)
        print("Experience:",self.exp,"years.")


p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()