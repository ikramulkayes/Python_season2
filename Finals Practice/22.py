class Bus:
    def __init__(self,name,dic):
        self.name = name
        self.faredic = dic
        self.dic = {}
        self.totalsell = 0
        self.totalpassengers = 0
    def addPassenger(self,*args):
        for elm in args:
            if elm.destination in self.faredic.keys():
                if elm.destination not in self.dic.keys():
                    self.dic[elm.destination] = [elm.name]
                else:
                    temp = self.dic[elm.destination]
                    temp.append(elm.name)
                    self.dic[elm.destination] = temp
                
                print(f"{elm.name} get into the bus")
                self.totalsell += self.faredic[elm.destination]
                self.totalpassengers += 1
            else:
                print(f"Sorry {elm.name}, the bus won’t go to {elm.destination}")
    def showDetail(self):
        print(f"Total ticket sell: {self.totalsell} Taka")
        print(f"Total passenger: {self.totalpassengers}")
        for k,v in self.dic.items():
            s = k +": "
            for elm in v:
                s += elm + ", "
            s = s.rstrip(", ")
            print(s)
    def dropPassesger(self,destination):
        self.totalpassengers -= len(self.dic[destination])
        del self.dic[destination]
        print(f"All passengers of {destination} are dropped")




class Passenger:
    def __init__(self,name,destination):
        self.name = name
        self.destination = destination






b=Bus("Volvo",{"Chittagong":1200,"Cumilla":700,"CoxBazar":1500})
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
b.dropPassesger("Cumilla")
print("9=============================")
b.showDetail()
print("10=============================")
b.dropPassesger("Chittagong")
print("11============================")
b.showDetail()