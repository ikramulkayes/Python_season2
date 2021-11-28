class Team:
    def __init__(self,name):
        self.cname = name
        self.dic = {}
        self.infodic = {}
    def addPlayer(self,*args):
        for elm in args:
            if elm.num == None:
                if type(elm.role) == str:
                    print("A player cannot be added without a jursey number.")
                else:
                    print("A player cannot be added without a role.")
            else:
                print(f"{elm.name} added in team")
                if elm.role not in self.infodic.keys():
                    self.infodic[elm.role] = f"Player name: {elm.name} Jersey No: {elm.num}" + "\n"
                else:
                    self.infodic[elm.role] += f"Player name: {elm.name} Jersey No: {elm.num}" +"\n"
    def showPlayers(self):
        for k,v in self.infodic.items():
            print(k+":")
            v = v.rstrip("\n ")
            print(v)
        
        

    

class Player:
    def __init__(self,name,role,num = None):
        self.name = name
        self.role = role
        self.num = num
    def setRole(self,role):
        if type(self.role) == int:
            self.num = self.role
            self.role = role


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
p3.setRole("Batsman")
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
    
