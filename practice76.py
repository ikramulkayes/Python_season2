class Traveller:
    count = 0
    def __init__(self,name):
        self.name = name
        Traveller.count += 1
        self.movie = ""
        self.cost = 0
    def buyTickets(self,*args):
        count = 1
        for elm in args:
            if count % 2 ==0:
                self.cost += elm
            else:
                self.movie += elm + ", "
            count += 1
    def printDetail(self):
        print("Name:",self.name)
        print("Tickets:",self.movie.rstrip(", "))
        print("Cost:",self.cost)

print("Total Traveller:", Traveller.count)
t1 = Traveller("Naruto")
t1.buyTickets("Mist Village",5000,"Rain Village", 10000)
t2 = Traveller("Minato")
t2.buyTickets("Cloud Village",15000,"Sand Village",1200,"Stone Village",  
5000)
t3 = Traveller("Kushina")
t3.buyTickets("Leaves Village", 3000)
print("=========================")
t1.printDetail()
print("=========================")
t2.printDetail()
print("=========================")
t3.printDetail()
print("=========================")
print("Total Traveller:", Traveller.count)