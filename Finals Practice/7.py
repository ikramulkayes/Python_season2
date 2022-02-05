class Transport:
    total_traveller = 0
    
    def __init__(self, name, fare):
        self.name = name
        self.baseFare = fare
    
    def __str__(self):
        s =  "Name: "+self.name+", Base fare: "+str(self.baseFare)
        return s

class Bus(Transport):
    def __init__(self, name, fare):
        super().__init__(name, fare)
        self.dic = {}
        print(f"Base-fare of {self.name} is {self.baseFare} Taka")
    def addPassengerWithBags(self,*args):
        count = 0
        for elm in range(0,len(args),2):
            self.dic[args[count]] = args[count+1]
            count += 2
            Transport.total_traveller += 1
    def __str__(self):
        k =  super().__str__()
        print(k)
        print(f"Total Passenger(s): {len(self.dic)}")
        print(f"Passenger details:")
        final = ""
        for k,v in self.dic.items():
            fare = self.baseFare
            if v <3:
                pass
            elif v <6:
                fare += 60
            else:
                fare += 105
            final +=f"Name: {k}, Fare: {fare}\n"
        final = final.rstrip("\n")
        return final
class Train(Bus):
    def __init__(self, name, fare):
        super().__init__(name, fare)

# Write your codes here.
# Do not change the following lines of code.
t1 = Bus("Volvo", 950)
print("=================================")
t1.addPassengerWithBags("David", 6,  "Mike", 1, "Carol", 3)
print("=================================")
print(t1)
print("=================================")
t2 = Train("Silk City", 850)
print("=================================")
t2.addPassengerWithBags("Bob", 2, "Simon", 4)
print("=================================")
print(t2)
print("=================================")
print("Total Passengers in Transport: ", Transport.total_traveller )
