class Anime:
    def __init__(self, name, rating, genre):
        self.name = name
        self.rating = rating
        self.genre = genre

    def add_character(self, *info):
        pass

    def __str__(self):
        s = f"Name: {self.name}\nRating: {self.rating}\nGenre: {self.genre}"
        return s

#Write your code here
class Naruto(Anime):
    def __init__(self, name, rating, genre,year):
        super().__init__(name, rating, genre)
        self.year = year
        self.dic = {}
    def add_character(self, *info):
        for elm in range(0,len(info),2):
            if info[elm+1] not in self.dic.keys():
                self.dic[info[elm+1]] = [info[elm]]
            else:
                temp = self.dic[info[elm+1]]
                temp.append(info[elm])
                self.dic[info[elm+1]] = temp
    def release_year(self):
        return f"{self.name} has been released in {self.year}!!!"
    def __str__(self):
        print("Anime Details:")
        print(super().__str__())
        s = f"Release Year:{self.year}\n"
        s+="Characters:\n"
        for k,v in self.dic.items():
            s += f"{k}: {v}\n"
        return s.rstrip("\n")
class MyHeroAcademia(Anime):
    def __init__(self, name, rating, genre,year):
        super().__init__(name, rating, genre)
        self.year = year
        self.dic = {}
    def add_character(self, *info):
        for elm in range(0,len(info),2):
            if info[elm] not in self.dic.keys():
                self.dic[info[elm]] = [info[elm+1]]
            else:
                temp = self.dic[info[elm]]
                temp.append(info[elm+1])
                self.dic[info[elm]] = temp
    def season_status(self):
        return f"My Hero Academia has premiered {self.year} seasons!!!"
    def __str__(self):
        print("Anime Details:")
        print(super().__str__())
        s = f"Season Premiered:{self.year}\n"
        s+="Characters:\n"
        for k,v in self.dic.items():
            s += f"{k}: {v}\n"
        return s.rstrip("\n")
    
    




# Do not change the following lines of code.

naruto = Naruto("Naruto", 10, "Adventure Fiction", 2007)
naruto.add_character("Naruto Uzumaki", "Main", "Itachi Uchiha", "Main", "Madara Uchiha", "Anti Hero", "Pain", "Supporting", "Shikamaru Nara", "Supporting")
print('1.------------------------------------')
print(naruto.release_year())
print('2.------------------------------------')
print(naruto)
print('3.====================================')
my_hero_academia = MyHeroAcademia("My Hero Academia", 8, "Superhero Fiction", 5)
my_hero_academia.add_character("Supporting", "Uraraka", "Anti Hero", "Nomu", "Supporting", "Mirio", "Main", "Midoriya", "Main", "Todoroki")
print('4.------------------------------------')
print(my_hero_academia.season_status())
print('5.------------------------------------')
print(my_hero_academia)