class Team:
    def __init__(self,name,wins,lang="Spanish"):
        self.name = name
        self.wins = wins
        self.lang = lang
        self.totalcost = 0
        self.dic = {}
        self.lst = []
        self.word = "["
    def player_list(self):
        if len(self.lst) == 0:
            print("No players assigned yet")
        else:
            print(self.lst.copy())
    def calculateCost(self):
        if self.totalcost == 0:
            print("No cost yet as there is no players")
        else:
            print(f"Total Cost: {self.totalcost}")


        
    def printDetail(self):
        print(f"Team Name: {self.name}")
        print(f"World Cup Win: {self.wins}")
        print(f"Language: {self.lang}")
        for k,v in self.dic.items():
            print(k+":")
            print(v)
    def addPlayer(self,player):
        if player.role == "Forward":
            self.totalcost += 500
        elif player.role == "Defender":
            self.totalcost += 450
        else:
            pass
        if player.role not in self.dic.keys():
            self.dic[player.role] = player.name + "\n"
        else:
            self.dic[player.role] += player.name + "\n"
        p = player.name
        r = player.role
        tt = (str(p),str(r))
        tt = tuple(tt)
        self.lst.append(tt)

            



class Player:
    def __init__(self,name,role = "Forward"):
        self.name = name
        self.role = role
    

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