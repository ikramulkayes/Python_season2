class Motorcycle:
    count = 0
    def __init__(self,name,year):
        self.name = name
        self.year = year
        self.services = ""
        Motorcycle.count += 1
    def add_Services(self,*args):
        for elm in args:
            self.services += elm + ", "
    def printMotorcycleDetail(self):
        print("Name:",self.name)
        print("Year of manufacture:",self.year)
        print("Services:",self.services.rstrip(", "))


print('No. of Motorcycle =', Motorcycle.count)
m1 = Motorcycle('Yamaha MT-15', 2019)
m1.add_Services('Oil change', 'Replace coolant')
m2 = Motorcycle('Suzuki V-Strom 650', 2020)
m2.add_Services('Rear suspension check', 'New air filter', 'Oil change')
m3 = Motorcycle('Honda Gold Wing', 2017)
m3.add_Services('Adjustment of throttle and clutch', 'New oil filter')
print("=========================")
m1.printMotorcycleDetail()
print("=========================")
m2.printMotorcycleDetail()
print("=========================")
m3.printMotorcycleDetail()
print("=========================")
print('No. of Motorcycle =', Motorcycle.count)
                
    