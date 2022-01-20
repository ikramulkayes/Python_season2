class Food:
    def __init__(self, name, rich_in):
        self.name = name
        self.rich_in = rich_in

    def __str__(self):
        s = f"Name: {self.name}\nRich in {self.rich_in}"
        return s

# Write your codes here.
class Vegetable(Food):
    def __init__(self, name, rich_in,money):
        super().__init__(name, rich_in)
        self.money = money
        self.dic = {}
        self.count = 0
    def add_Vegetables(self,*args):
        for elm in args:
            k = elm.split(" ")[0]
            elm = elm.strip(k)
            elm = elm.strip()
            if k.capitalize() not in self.dic.keys():
                self.dic[k.capitalize()] = [elm]
            else:
                temp = self.dic[k.capitalize()]
                temp.append(elm)
                self.dic[k.capitalize()] = temp
            self.count += int(elm.split("-")[1][1])
    def show_Cost(self):
        print(f"{self.name} , total cost: {self.count*self.money} BDT")
    def __str__(self):
        print(super().__str__())
        s = f"Price: {self.money} BDT per kg\n"
        s += "Vegetable Details:\n"
        for k,v in self.dic.items():
            s+= f"{k} : {v}\n"
        s = s.rstrip("\n")
        return s
class Fruit(Food):
    def __init__(self, name, rich_in,money):
        super().__init__(name, rich_in)
        self.money = money
        self.dic = {}
        self.count = 0
    def add_Fruits(self,*args):
        for elm in args:
            k = elm.split(" ")[0]
            elm = elm.strip(k)
            elm = elm.strip()
            if k.capitalize() not in self.dic.keys():
                self.dic[k.capitalize()] = [elm]
            else:
                temp = self.dic[k.capitalize()]
                temp.append(elm)
                self.dic[k.capitalize()] = temp
            self.count += int(elm.split("-")[1][1])
    def show_Cost(self):
        print(f"{self.name} , total cost: {self.count*self.money} BDT")
    def __str__(self):
        print(super().__str__())
        s = f"Price: {self.money} BDT per kg\n"
        s += "Fruit Details:\n"
        for k,v in self.dic.items():
            s+= f"{k} : {v}\n"
        s = s.rstrip("\n")
        return s



    






# Do not change the following lines of code.

g1 = Vegetable("Tomato", "folate, vitamin C, and potassium", 60)
g1.add_Vegetables("Red large Tomato - 5kg","Green small tomato - 2kg","red Medium Tomato - 3kg","green Large tomato - 2kg","Yellow Medium Tomato - 1kg")
print('====================================')
g1.show_Cost()
print('====================================')
print(g1)
print('====================================')
g2 = Fruit("Apple", "fiber, vitamin C, and various antioxidants", 90)
g2.add_Fruits("Red small Apple - 9kg", "Green small Apple - 5kg", "red Large Apple - 9kg")
print('====================================')
g2.show_Cost()
print('====================================')
print(g2)