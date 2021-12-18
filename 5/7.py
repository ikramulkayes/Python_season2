class Dolls:
    def __init__(self, name = "", num = 0):
        self.__name = name
        self.__num = num
    def detail(self):
        print(f"Doll: {self.__name}")
        return f"Total Price: {self.__num} taka"
    def setName(self,name):
        self.__name = name
    def setNumber(self,number):
        self.__num = number
        
    def __add__(self,other):
        obj = Dolls()
        obj.setName(self.__name +" "+ other.__name)
        obj.setNumber(self.__num+other.__num)
        return obj
    def __gt__(self,other):
        if self.__num > other.__num:
            return True
        else:
            return False


obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

