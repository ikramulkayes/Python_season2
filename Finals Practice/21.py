# Write you code here
class Vehicle:
    def __init__(self,number,vehicle,name,farechart):
        self.number = number
        self.vehicle = vehicle
        self.name = name
        self.farechart = farechart
        self.lst = []
    def addPassenger(self,*args):
        for elm in args:
            if elm.destination in self.number:
                if elm.money == None:
                    if self.name in self.farechart.keys():
                        elm.money = self.farechart[self.name]
                    else:
                        elm.money = self.farechart["Others"]
                self.lst.append(f"Passenger name : {elm.name}, Destination: {elm.destination}, Ticket Price:{elm.money} ")
                print(f"{elm.name} has taken the {self.vehicle}")
            else:
                print(f"This is an Inter-City {self.vehicle}. {elm.name} cannot take the {self.vehicle}.")

    def status(self):
        print(f"Details of {self.number} {self.vehicle} of {self.name}:")
        print(f"Total Passengers: {len(self.lst)}")
        for elm in self.lst:
            print(elm)


class Passenger:
    def __init__(self,name,destination=None):
        self.name = name
        self.destination = destination
        self.money = None
        if self.destination == None:
            print("Destination cannot be empty!")
    def calculateFare(self,obj):
        if obj.name in obj.farechart.keys():
            self.money = obj.farechart[obj.name]
        else:
            self.money = obj.farechart["Others"]
        print(f"Calculating fare for {self.name}")
    def setDestination(self,destination):
        self.destination = destination
        print(f"Destination of {self.name} is updated to {self.destination}")
    


#=================================================
#Do not change the codes below

fareChart = {'SR Travels': 40, 'ENA': 50, 'Pathao': 200, 'Uber': 
250, 'Hanif Paribahan': 45, 'Others': 90 }
v1 = Vehicle("Dhaka-123", "Bus", 'SR Travels', fareChart)
p1 = Passenger("Sam", "Dhaka")
print("1.===========================")
v1.addPassenger(p1)
print("2.===========================")
p1.calculateFare(v1)
print("3.===========================")
p2 = Passenger("John", "Dhaka")
p3 = Passenger("Bran")
print("4.===========================")
p3.setDestination("Chittagong")
print("5.===========================")
v1.addPassenger(p2, p3)
print("6.===========================")
p2.calculateFare(v1)
print("7.===========================")
p4 = Passenger("Mark", "Dhaka")
p5 = Passenger("Jack", "Khulna")
v1.addPassenger(p4, p5)
print("8.===========================")
p4.calculateFare(v1)
print("===========================")
v1.status()
v2 = Vehicle("Chittagong-798", "Car", "Uber", fareChart)
print("9.===========================")
v2.addPassenger(p1)
v2.addPassenger(p3)
print("10.===========================")
p3.calculateFare(v2)
print("11.===========================")
v2.status()
v3 = Vehicle("Khulna-997", "Car", "Obhai", fareChart)
v3.addPassenger(p5)
print("12.===========================")
p5.calculateFare(v3)
print("13.===========================")
v3.status()