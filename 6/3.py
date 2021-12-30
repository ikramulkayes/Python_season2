class Passenger:
    count = 0
    def __init__(self,name):
        self.name = name
        self.weight = 0
        Passenger.count += 1
    def set_bag_weight(self,weight):
        self.weight = weight
    def printDetail(self):
        self.busfare = 450
        if self.weight >20 and self.weight<=50:
            self.busfare += 50
        elif self.weight >50:
            self.busfare += 100
        print("Name:",self.name)
        print("Bus Fare:",self.busfare)

print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)
    
    