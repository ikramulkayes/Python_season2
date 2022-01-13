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
        Squad.playerCount+= 1
        for elm in args:

            if elm[1] not in self.dic.keys():
                self.dic[elm[1]] =[[elm[0],elm[2]]]
            else:
                temp = self.dic[elm[1]] 
                temp.append([[elm[0],elm[2]]])
                self.dic[elm[1]] = temp
    def __str__(self):
        s =  super().__str__() + "\n"
        
        for key,val in self.dic.items():
            print(key+":")
            for selm in val:
                s+= f"Player name: {selm[0]}, House: {selm[1]}\n"
            return s.rstrip("\n")
        
    def formSquad(self):
        
        if super().formSquad():
            print("We have enough players to form a squad")
            count = 0
            if len(self.dic["Beater"]) >= 2:
                if len(self.dic["Chaser"]) >= 1:
                    if len(self.dic["Seeker"])>=1:
                        if len(self.dic["Keeper"])>=1:
                            print("Also we can form a perfect squad!!.")
                            
                        else:
                            print("But we cannot form a perfect squad.")
                    else:
                        print("But we cannot form a perfect squad.")
                else:
                    print("But we cannot form a perfect squad.")
            else:
                print("But we cannot form a perfect squad.")



        else:
            print("We do not have enough players to form a squad.")
        
            
                



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
