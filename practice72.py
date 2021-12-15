class SultansDine:
    branchcount = 0
    totalsell = 0
    lst = []
    def __init__(self,name):
        self.name = name
        self.Branch_sell = 0
        SultansDine.branchcount += 1
        
    def sellQuantity(self,num):
        if num < 10:
            self.Branch_sell = num*300
        elif num < 20:
            self.Branch_sell = num*350
        else:
            self.Branch_sell = num*400
        SultansDine.totalsell += self.Branch_sell
        SultansDine.lst.append([self.name,self.Branch_sell])
    def branchInformation(self):
        print(f"Branch Name: {self.name}")
        print(f"Branch Sell: {self.Branch_sell} Taka")
    
    @classmethod
    def details(cls):
        print("Total Number of brach(s):",cls.branchcount)
        print("Total Sell::",cls.totalsell) 
        if len(cls.lst)>0:
            for elm in cls.lst:
                percent = (elm[1]/cls.totalsell)*100
                percent = round(percent,)
                print(f"Branch Name: {elm[0]}, Branch Sell: {elm[1]} Taka") 
                print(f"Branch consists of total sell's: {percent}%")  


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
