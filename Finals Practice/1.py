class Bird:
    def __init__(self,name,can = False):
        self.name = name
        self.can = can
    def fly(self):
        if self.can == True:
            print(f"{self.name} can fly")
            self.type = "Flight Birds"
        else:
            print(f"{self.name} can not fly")
            self.type = "Flightless Birds"
    def setType(self,type):
        self.type = type
    def printDetail(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")





ostrich = Bird('Ostrich')
duck = Bird("Duck", True)
owl = Bird('Owl', True)
print("###########################")
ostrich.fly()
duck.fly()
owl.fly()
duck.setType('Water Birds')
owl.setType('Birds of Prey')
print("=========================")
ostrich.printDetail()
print("=========================")
duck.printDetail()
print("=========================")
owl.printDetail()
