class Series:
    def __init__(self,name,year,country = "English"):
        self.name = name
        self.year = year
        self.country = country
        self.character_list = "No characters assigned yet"
        self.cost = 0
        self.dic = {}
    def calculateCost(self):
        if self.cost ==0:
            print("No cost yet as there is no characters")
        else:
            print("Total Cost: ",self.cost)
    def addCharacter(self,obj):
        if type(self.character_list) == str:
            self.character_list = [(obj.name , obj.role)]
        else:
            self.character_list.append([obj.name,obj.role])
        if obj.role == "Main character":
            self.cost += 10000
        else:
            self.cost += 5000
        if obj.role not in self.dic.keys():
            self.dic[obj.role] = obj.name + "\n"
        else:
            self.dic[obj.role] += obj.name + '\n'
    def printDetail(self):
        print("Series Name:",self.name)
        print("Release Year:",self.year)
        print("Language:",self.country)
        if type(self.character_list) == list:
            print("Main Characters(s):")
            print(self.dic["Main character"].rstrip("\n"))  
            print("Supporting Characters(s):")
            print(self.dic["Supporting character"].rstrip("\n"))    
class Character:
    def __init__(self,name,role="Supporting character"): 
        self.name = name
        self.role = role



# Write you code here
sherlock = Series("Sherlock Holmes", 2010)
print("1.============================================")
print(sherlock.character_list)
print("2.============================================")
sherlock.calculateCost()
print("3.============================================")
sherlock.printDetail()
print("4.============================================")
holmes = Character("Sherlock Holmes", "Main character")
watson = Character("James Watson", "Main character")
irene = Character("Irene Adler")
sherlock.addCharacter(holmes)
sherlock.addCharacter(watson)
sherlock.addCharacter(irene)
print("5.============================================")
sherlock.calculateCost()
print("6.============================================")
sherlock.printDetail()
print("7.============================================")
print(sherlock.character_list)
print("8.###############################################")
squid_games = Series("Squid Games", 2021, "Korean")
print("9.============================================")
print(squid_games.character_list)
print("10.============================================")
squid_games.calculateCost()
print("11.============================================")
squid_games.printDetail()
print("12.============================================")
seong = Character("Seong", "Main character")
kang = Character("Kang")
squid_games.addCharacter(seong)
squid_games.addCharacter(kang)
print("13.============================================")
squid_games.calculateCost()
print("14.============================================")
squid_games.printDetail()
print("15.============================================")
print(squid_games.character_list)