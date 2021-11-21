class Hotel:
    def __init__(self,hotel):
        self.hotel = hotel
        self.dic = {}
        self.gdic = {}
        self.scount = 0
        self.gcount = 0
    def addStuff(self,name,age,phone="000"):
        self.scount += 1
        self.dic[self.scount] = {"Stuff ID": self.scount,
                                "Name": name,
                                "Age":    age,
                                "Phone no":phone
                                    
                                    }
        print(f"Staff With ID {self.scount} is added")
    def addGuest(self,name,age,phone="000"):
        self.gcount += 1
        self.gdic[self.gcount] = {"Guest ID": self.gcount,
                                "Name": name,
                                "Age":    age,
                                "Phone no":phone
                                    
                                    }
        print(f"Guest With ID {self.gcount} is created")
    def getStuffById(self,id):
        tempdic = self.dic[id]
        final = ""
        for k,v in tempdic.items():
            final +=k+": "+str(v) +"\n"
        return final.rstrip("\n")
    def getGuestById(self,id):
        tempdic = self.gdic[id]
        final = ""
        for k,v in tempdic.items():
            
            final += k+": "+str(v) +"\n"
        return final.rstrip("\n")
    def allStaffs(self):
        print("All Staffs:")
        print(f"Number of Staff",self.scount)
        for id in range(1,self.scount+1):
            tempdic = self.dic[id]
            final = ""
            for k,v in tempdic.items():
                
                final += k+": "+str(v)+" " 
            print(final)
    def allGuest(self):
        print("All Guest:")
        print(f"Number of Guest",self.gcount)
        for id in range(1,self.gcount+1):
            tempdic = self.gdic[id]
            final = ""
            for k,v in tempdic.items():
                
                final += k+": "+str(v) +" "
            print(final)
        


h = Hotel("Lakeshore")
h.addStuff( "Adam", 26)
print("=================================")
print(h.getStuffById(1))
print("=================================")
h.addGuest("Carol",35,"123")
print("=================================")
print(h.getGuestById(1))
print("=================================")
h.addGuest("Diana", 32, "431")
print("=================================")
print(h.getGuestById(2))
print("=================================")
h.allStaffs()
print("=================================")
h.allGuest()
        