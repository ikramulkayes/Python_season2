class Team:
    def __init__(self,name,cup,lang="Spanish"):
        self.name = name
        self.cup = cup
        self.player_list = "No players assigned yet"
        self.cost = 0
        self.dic = {"Forward":"","Defender":""}
        self.lang = lang
    def calculateCost(self):
        if type(self.player_list) == list:
            print("Total Cost:",self.cost)
        else:
            print("No cost yet as there is no players")
    def addPlayer(self,obj):
        if type(self.player_list) == str:
            self.player_list = [(obj.name,obj.role)]
        else:
            self.player_list.append((obj.name,obj.role))
        if obj.role == "Forward":
            self.cost += 500
        else:
            self.cost += 450
        
        self.dic[obj.role] += obj.name + "\n"
        
    def printDetail(self):
        print("Team Name:",self.name)
        print("World Cup Win:",self.cup)
        print("Language:",self.lang)
        if type(self.player_list) == list:
            print("Forwards:")
            print(self.dic["Forward"].rstrip("\n"))
            print("Defenders:")
            print(self.dic["Defender"].rstrip("\n"))





class Player:
    def __init__(self,name,role="Forward"):
        self.name = name
        self.role = role


# Write you code here
argentina = Team("Argentina", 2)
print("1.============================================")
print(argentina.player_list)
print("2.============================================")
argentina.calculateCost()
print("3.============================================")
argentina.printDetail()
print("4.============================================")
messi = Player("Messi")
maria = Player("Maria")
marcos = Player("Marcos", "Defender")
argentina.addPlayer(messi)
argentina.addPlayer(maria)
argentina.addPlayer(marcos)
print("5.============================================")
argentina.calculateCost()
print("6.============================================")
argentina.printDetail()
print("7.============================================")
print(argentina.player_list)
print("8.###############################################")
brazil = Team("Brazil", 5, "Portuguese")
print("9.============================================")
print(brazil.player_list)
print("10.============================================")
brazil.calculateCost()
print("11.============================================")
brazil.printDetail()
print("12.============================================")
silva = Player("Silva", "Defender")
neymar = Player("Neymar")
brazil.addPlayer(silva)
brazil.addPlayer(neymar)
print("13.============================================")
brazil.calculateCost()
print("14.============================================")
brazil.printDetail()
print("15.============================================")
print(brazil.player_list)
