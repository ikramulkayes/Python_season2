class bird:
    def __init__(self):
        print("A bird is flying in the sky")
b1 =bird()


class animal:
    pass
tiger = animal()
print(tiger)

class student:
    def __init__(self,name):
        self.name = name
stu1 = student("Edward")
stu2 = student("Elizabeth")
stu4 = student("Philip")
#print(stu3.name, "is very attentive and studious")

class wizard:
    def __init__(self,name):
        self.name = name
wiz1 = wizard("Severus")
wiz2 = wizard("Albus")
print("The name of the professor is ",wiz2.name)