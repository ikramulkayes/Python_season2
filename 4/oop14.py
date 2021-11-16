class EPL_Team:
    def __init__(self,name,slogan="No Slogan",title=0):
        self.name = name
        self.slogan = slogan
        self.title = title
    def increaseTitle(self):
        self.title += 1
    def changeSong(self,song):
        self.slogan = song
    def showClubInfo(self):
        final = ""
        final += "Name: "+self.name +"\n"
        final += "Song: "+self.slogan+"\n"
        final += "Total No of title: "+str(self.title)
        return final


manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())
    