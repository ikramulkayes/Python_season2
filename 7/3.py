class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
#write your code here

class Cricket_Tournament(Tournament):
    def __init__(self, name='Default',teams = 0,type = "No type"):
        super().__init__(name=name)
        self.name = super().get_name()
        self.team = teams
        self.type = type
    def detail(self):
        print("Cricket Tournament Name:",self.name)
        print("Number of Teams:",self.team)
        return f"Type: {self.type}"

class Tennis_Tournament(Tournament):
    def __init__(self, name='Default',no_of_player=0):
        super().__init__(name=name)
        self.name = super().get_name()
        self.no_of_players = no_of_player
    def detail(self):
        print("Tennis Tournament Name:",self.name)
        return f"Number of Players: {self.no_of_players}"




ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())