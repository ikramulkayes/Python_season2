class SultansDine:
    branchnum = 0
    totalsell = 0
    selllist = []
    def __init__(self,name):
        self.name = name
        SultansDine.branchnum += 1
    def sellQuantity(self,sell):
        if sell < 10:
            fsell = sell*300
        elif sell < 20:
            fsell = sell*350
        else:
            fsell = sell*400
        self.sell = fsell
        
        SultansDine.totalsell += fsell
        SultansDine.selllist.append([self.name,self.sell])
    def branchInformation(self):
        print(f"Branch Name: {self.name}")
        print(f"Total Sell: {self.sell} Taka")

    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {SultansDine.branchnum}")
        print(f"Total sell: {SultansDine.totalsell}")
        for elm in SultansDine.selllist:
            print(f"Branch Name: {elm[0]}, Branch Sell: {elm[1]} Taka")
            print(f"Branch consists of total sell's: {round((elm[1]/SultansDine.totalsell)*100,2)}%")

SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()

