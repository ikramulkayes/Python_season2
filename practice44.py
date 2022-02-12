class OlympicCountry:
    def __init__(self,name):
        self.cname = name
        self.count = 0
        self.mdic = {"Gold":[],"Silver":[],"Bronze":[]}
    def add_player(self,*args):
        for elm in args:
            if elm.medal == None:
                print("A player must have a medal. Add the medal first")
            else:
                self.count += 1
                temp = self.mdic[elm.medal]
                temp.append(elm.name)
                self.mdic[elm.medal] = temp
    def show_medal_info(self):
        print(f"Total medals won by {self.cname} is {self.count}")
        print("**")
        for k,v in self.mdic.items():
            print(k,v)
                



class AwardedPlayer:
    def __init__(self,name,medal = None):
        self.name = name
        self.medal = medal
    def add_medal(self,medal):
        self.medal = medal
    
    


country1 = OlympicCountry('Jamaica')
country2 = OlympicCountry('USA')
player1 = AwardedPlayer('Usain Bolt')
player2 = AwardedPlayer('Shelly-Ann Fraser-Pryce','Silver')
player3 = AwardedPlayer('Elaine Thompson Herah','Gold')
player4 = AwardedPlayer('Michael Phelps','Gold')
player5 = AwardedPlayer('Caeleb Dressel','Gold')
print('-----------------------------------------')
country1.add_player(player1)
print('-----------------------------------------')
player1.add_medal('Gold')
country1.add_player(player1)
country1.add_player(player2)
country1.add_player(player3)
print('-----------------------------------------')
country1.show_medal_info()
print('-----------------------------------------')
country2.add_player(player4)
country2.add_player(player5)
print('-----------------------------------------')
country2.show_medal_info()