class Cat:
    def __init__(self,color = "White",state= "sitting"):
        self.color = color
        self.state = state
    def changeColor(self,color):
        self.color = color
    def printCat(self):
        print(f"{self.color} cat is {self.state}")


c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()