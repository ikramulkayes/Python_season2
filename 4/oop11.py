class Shinobi:
    def __init__(self,name,rank):
        self.name = name
        self.rank = rank
        self.salary = 0
        self.mission = 0
    def changeRank(self,rank):
        self.rank = rank
    def calSalary(self,mission):
        self.mission = mission
        if self.rank == "Genin":
            self.salary = mission*50
        elif self.rank == "Chunin":
            self.salary = mission*100
        else:
            self.salary = mission*500
    def printInfo(self):
        print("Name:",self.name)
        print("Rank:",self.rank)
        print("Number of mission:",self.mission)
        print("Salary:",self.salary)



naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()