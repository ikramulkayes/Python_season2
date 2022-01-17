class Actor:
    def __init__(self, name, rating, industry):
        self.name = name
        self.rating = rating
        self.industry = industry

    def add_movie(self, *info):
        pass

    def __str__(self):
        s = f"Name: {self.name}\nRating: {self.rating}\nIndustry: {self.industry}"
        return s

#Write your code here
class TomCruise(Actor):
    def __init__(self, name, rating, industry,award):
        super().__init__(name, rating, industry)
        self.oscar = award
        self.dic = {}
    def add_movie(self, *info):
        for elm in range(0,len(info),2):
            if info[elm+1] not in self.dic.keys():
                self.dic[info[elm+1]] = [info[elm]]
            else:
                temp = self.dic[info[elm+1]]
                temp.append(info[elm])
                self.dic[info[elm+1]] = temp
    def __str__(self):
        print(super().__str__())
        s = ""
        s += f"Oscar Win {self.oscar}\n"
        s += "Movies:\n"
        for k,v in self.dic.items():
            s += f"{k}: {v}\n"
        return s.rstrip("\n")
    def oscar_status(self):
        return(f"Tom Cruise has won {self.oscar} Oscar(s)!!!")


class DulquerSalman(Actor):
    def __init__(self, name, rating, industry,award):
        super().__init__(name, rating, industry)
        self.award = award
        self.dic = {}
    def add_movie(self, *info):
        for elm in range(0,len(info),2):
            if info[elm] not in self.dic.keys():
                self.dic[info[elm]] = [info[elm+1]]
            else:
                temp = self.dic[info[elm]]
                temp.append(info[elm+1])
                self.dic[info[elm]] = temp
    def __str__(self):
        print(super().__str__())
        s = ""
        s += f"Award Win {self.award}\n"
        s += "Movies:\n"
        for k,v in self.dic.items():
            s += f"{k}: {v}\n"
        return s.rstrip("\n")
    def award_status(self):
        return(f"Dulquer Salman has won {self.award} award(s)!!!")       




# Do not change the following lines of code.

tom_cruise = TomCruise("Tom Cruise", 9.5, "Hollywood", 0)
tom_cruise.add_movie("Knight & Day", "Action", "Top Gun", "Action", "Jerry Maguire", "Romance", "Jack Reacher", "Thriller", "The Firm", "Thriller")
print('1.------------------------------------')
print(tom_cruise.oscar_status())
print('2.------------------------------------')
print(tom_cruise)
print('3.====================================')
dulquer_salman = DulquerSalman("Dulquer Salman", 9, "Malayalam", 5)
dulquer_salman.add_movie("Thriller", "Bangalore Days", "Romance", "Ustad Hotel", "Thriller", "Charlie", "Action", "Kurup", "Action", "Vikramadithyan")
print('4.------------------------------------')
print(dulquer_salman.award_status())
print('5.------------------------------------')
print(dulquer_salman)