class Batsman:
    def __init__(self,*args):
        if type(args[0]) == str:
            self.name = args[0]
            self.run = args[1]
            self.ball = args[2]
        else:
            self.name = "New Batsman"
            self.run = args[0]
            self.ball = args[1]
    def setName(self,name):
        self.name = name
    def battingStrikeRate(self):
        return (self.run/self.ball)*100
    def printCareerStatistics(self):
        print("Name:",self.name)
        print("Runs Scored:",self.run,", Balls Faced",self.ball)


b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())

