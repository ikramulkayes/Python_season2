class Smartphone:
    def __init__(self,name=None):
        self.name = name
        self.display = ""
        self.ram = ""
    def setName(self,name):
        self.name = name
    def addFeature(self,fname,f):
        if fname == "Display":
            if self.display.rstrip(", ") != f:
                self.display += f +', '
        elif fname =="Ram":
            self.ram += f+', '
    def printDetail(self):
        print(f"Phone Name: {self.name}")
        if self.display != "":
            self.display = self.display.rstrip(", ")
            print(f"Display: {self.display}")
            self.display = self.display + ", "
        if self.ram != "":
            self.ram = self.ram.rstrip(", ")
            print(f"Ram: {self.ram}")
            self.ram = self.ram +", "

    





# Do not change the following lines of code.
s1 = Smartphone()
print("=================================")
s1.addFeature("Display", "6.1 inch")
print("=================================")
s1.setName("Samsung Note 20")
s1.addFeature("Display", "6.1 inch")
s1.printDetail()
print("=================================")
s2 = Smartphone("Iphone 12 Pro")
s2.addFeature("Display", "6.2 inch")
s2.addFeature("Ram", "6 GB")
print("=================================")
s2.printDetail()
s2.addFeature("Display", "Amoled panel")
s2.addFeature("Ram", "DDR5")
print("=================================")
s2.printDetail()
print("=================================")