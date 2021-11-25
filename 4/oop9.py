class Patient:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def add_Symptom(self,*args):
        word = "Symptoms: "
        for elm in args:
            word+= elm+", "
        self.word = word.rstrip(", ")
    def printPatientDetail(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print(self.word)


p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()
print("=========================")