class Player:
    database={}
    playerNo = 0
    def __init__(self,name,team,jerseyNo):
        self.name = name
        self.team = team
        self.jerseyNo = jerseyNo
    def __str__(self):
        return "Name:{}\nTeam:{}\nJersey No:{}".format(self.name,self.team,self.jerseyNo)

#Write your code here
class FootballPlayer(Player):

    def __init__(self, name, team, jerseyNo,goals=0,retirementdate="Not yet retired"):
        super().__init__(name, team, jerseyNo)
        self.goals = goals
        self.retirementdate = retirementdate
        Player.playerNo += 1
        name = name.split()
        self.id = str(str(Player.playerNo)+name[0][0]+name[1][0]+str(jerseyNo))
        super().database[self.id] = [self.name,team,jerseyNo,goals,retirementdate]
    def __str__(self):
        return f"Player ID: {self.id}\n"+ super().__str__()+f"\nGoals Scored: {self.goals}\nRetirement date: {self.retirementdate}"
    @classmethod
    def createPlayer(cls, name, team, jerseyNo,goals=0,retirementdate="Not yet retired"):
        obj = FootballPlayer(name, team, jerseyNo,goals,retirementdate)
        return obj
    




print("Number of players:",Player.playerNo)
print("Player Database:",Player.database)
print("#################################")
p1 = FootballPlayer("Lionel Messi","Barcelona",10,231)
print("------Details of the player------")
print(p1)
print("#################################")
p2 = FootballPlayer("Cristiano Ronaldo","Juventus",7,215)
print("------Details of the player------")
print(p2)
print("#################################")
p3 = FootballPlayer.createPlayer("Miroslav Klose","Lazio",11, 71,"11 Aug,2014")
print("------Details of the player------")
print(p3)
print("#################################")
print("Number of players:",Player.playerNo)
print("Player Database:",Player.database)
