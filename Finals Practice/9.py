class Squad:
    playerCount=0
    def __init__(self,name,squadType):
        self.name = name
        self.squadType = squadType
    def formSquad(self):
        if Squad.playerCount >= 5:
            return True
        else:
            return False
    def __str__(self):
        s = f"{self.name} is a {self.squadType} team.\n"
        s+= f"Number of players in {self.name} is {Squad.playerCount}\n"
        return s

#Write your code here
class HogwartsQuidditchSquad(Squad):
    def __init__(self, name, squadType):
        super().__init__(name, squadType)
        self.dic = {}
    def addPlayer(self,*args):
        for elm in args:
            if elm[1] not in self.dic.keys():
                self.dic[elm[1]] = [[elm[0],elm[2]]]
            else:
                temp = self.dic[elm[1]]
                temp.append([elm[0],elm[2]])
                self.dic[elm[1]] = temp
            Squad.playerCount += 1
    def __str__(self):
        print(super().__str__().rstrip("\n"))
        s = ""
        for k,v in self.dic.items():
            s += f"{k}s:\n"
            for elm in v:
                s+= f"Player name: {elm[0]}, House: {elm[1]}\n"
        s = s.rstrip("\n")
        return(s)
    def formSquad(self):
        if super().formSquad():
            print("We have enough players to form a squad.")
            flag = False
            if len(self.dic["Seeker"])>=1:
                if len(self.dic["Beater"])>=2:
                    if len(self.dic["Chaser"])>=1:
                        if len(self.dic["Keeper"])>=1:
                            flag = True
            if flag:
                print("Also we can form a perfect squad!!")
            else:
                print("But we cannot form a perfect squad.")
        else:
            print("We do not have enough players to form a squad.")
    
        
            
            




# Do not change the following lines of code.

f = HogwartsQuidditchSquad("Hogwart's Dragons","Quidditch")
f.addPlayer(["Harry Potter","Seeker","Gryffindor"],["Katie Bell","Chaser","Gryffindor"])
print("1.====================================")
print(f)
print("2.====================================")
f.formSquad()
print("3.====================================")
f.addPlayer(["Vincent Crabbe","Beater","Slytherin"])
f.addPlayer(["Miles Bletchley","Keeper","Slytherin"])
print("4.====================================")
print(f)
print("5.====================================")
f.formSquad()
print("6.====================================")
f.addPlayer(["Ethan Humberstone","Keeper","Hufflepuff"])
f.formSquad()
print("7.====================================")
f.addPlayer(["Fred Weasley","Beater","Gryffindor"])
print(f)
print("8.====================================")
f.formSquad()