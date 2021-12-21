class Assassin:
    assassinnum = 0
    def __init__(self,name,srate):
        self.name = name
        self.srate = srate
        Assassin.assassinnum += 1
    def printDetails(self):
        print("Name:",self.name)
        print(f"Success rate: {self.srate}%")
        print(f"Total number of Assassin: {Assassin.assassinnum}")
    @classmethod
    def failureRate(cls,name,frate):
        obj = cls(name,100-frate)
        return obj
    @classmethod
    def failurePercentage(cls,name,frate):
        obj = cls(name,100-frate)
        return obj
john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage('Akabane', 10)
akabane.printDetails()
