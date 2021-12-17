class Team:
    def __init__(self,name):
        self.county = name
        self.dic = {}
    def addPlayer(self,*args):
        for obj in args:
            print(f"{obj.name} added in team")
        
            self.dic[obj.name] = f"Jersey No: {obj.num}"
    def showPlayers(self):
        for k,v in self.dic.items():
            print("Player name:",k,v)
class Player:
    def __init__(self,name,role = None,code = None):
        self.name = name
        self.role = role
        self.num = code




team = Team("Bangladesh")
p1 = Player("Mahmudullah", "Batsman",30)
print("=================================")
team.addPlayer(p1)
print("=================================")
team.showPlayers()
print("=================================")
p2 = Player("Mustafizur Rahman", "Bowler",90)
p3 = Player("Tamim Iqbal", 28)
print("=================================")
team.addPlayer(p2,p3)
print("=================================")
team.showPlayers()
print("=================================")
#p3.setRole("Batsman")
print("=================================")
team.addPlayer(p3)
print("=================================")
team.showPlayers()
print("=================================")
p4 = Player("Mushfiqur Rahim", "Batsman",15)
p5 = Player("Taskin Ahmed", "Bowler",3)
print("=================================")
team.addPlayer(p4,p5)
print("=================================")
team.showPlayers()