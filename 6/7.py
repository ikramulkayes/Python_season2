class Cat:
    Number_of_cats = 0
    def __init__(self,color,doing):
        self.color = color
        self.doing = doing
        Cat.Number_of_cats += 1
    def printCat(self):
        print(f"{self.color} cat is {self.doing}")
    @classmethod
    def no_parameter(cls):
        obj = cls("White","sitting")
        return obj
    @classmethod
    def first_parameter(cls,color):
        obj = cls(color,"sitting")
        return obj
    @classmethod
    def second_parameter(cls,doing):
        obj = cls("Grey",doing)
        return obj
    def changeColor(self,color):
        self.color = color


print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)