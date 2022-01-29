
class Passenger:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Bus:
    def __init__(self, name, trips):
        self.name = name
        self.des = des
        self.list = []
        self.totalTicket = 0

    def addPassenger(self, *others):
        for i in other:
            if i.location in self.des:
                self.totalTicket += self.des[i.location]
                self.other.append(i)
                print(i.name + " get into the bus")
            else:
                print("Sorry " + i.name + ", the bus won’t go to " + i.location)

    def dropPassenger(self, location):
        for i in self.list:
            if (i.location == location):
                self.remove()
        print("All passengers of " + location + " are dropped")

    def showDetail(self):
        print("Total ticket sell: " + str(self.totalTicket) + " Taka")
        print("Total Passenger: " + str(len(self.list)))
        for i in self.list:
            value = []  
            for num in self.list:
                if num.location == i:
                    i.append(num.name)

            if (len(i) > 0):
                print(i + ": " + ", ".join(num))


b = Bus("Volvo", {"Chittagong": 1200, "Cumilla": 700, "CoxBazar": 1500})
p1 = Passenger("Bob", "Chittagong")
print("1=============================")
b.addPassenger(p1)
print("2=============================")
p2 = Passenger("Mike", "CoxBazar")
p3 = Passenger("Carol", "Barisal")
print("3=============================")
b.addPassenger(p2, p3)
print("4=============================")
b.showDetail()
print("5=============================")
p4 = Passenger("Alice", "Chittagong")
p5 = Passenger("David", "CoxBazar")
p6 = Passenger("Simon", "Cumilla")
p7 = Passenger("Tony", "Cumilla")
print("6=============================")
b.addPassenger(p4, p5, p6, p7)
print("7=============================")
b.showDetail()
print("8=============================")
b.dropPassenger("Cumilla")
print("9=============================")
b.showDetail()
print("10=============================")
b.dropPassenger("Chittagong")
print("11============================")
b.showDetail()