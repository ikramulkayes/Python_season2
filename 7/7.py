class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0
    def get_name_team(self):
        return 'Name: '+self.__name+', Team Name: ' +self.__team
#write your code here

class Player(Football):
    def __init__(self, team_name, name, role,goal,wins):
        super().__init__(team_name, name, role)
        self.goal = goal
        self.match = wins
        self.flag = False
    def calculate_ratio(self):
        self.ratio = self.goal/self.match
        self.flag = True
    def print_details(self):
        print(super().get_name_team())
        print(f"Team Role: {self.role}")
        print(f"Total Goal: {self.goal}, Total Played: {self.match}")
        if self.flag:
            print(f"Goal Ratio: {self.ratio}")
        print(f"Match Earning: {(self.goal)*1000 + (self.match)*10}k")
class Manager(Football):
    def __init__(self, team_name, name, role,wins):
        super().__init__(team_name, name, role)
        self.wins = wins
    def print_details(self):
        print(super().get_name_team())
        print(f"Team Role: {self.role}")
        print(f"Total Wins: {self.wins}")
        print(f"Match Earning: {self.wins*1000}k")






player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()