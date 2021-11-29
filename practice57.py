class Chocolates:
    def __init__(self):
        self.total = 0
        self.dic = {}
    

    def print_info(self):
        if self.total == 0:
            print("Number of chocolates: 0")
        else:
            print(f"Number of chocolates: {self.total}")
            for k,v in self.dic.items():
                print(f"{k}: {v}")
    
    def update_info(self,obj):
        key = obj.type
        if key not in self.dic.keys():
            self.dic[key] = [[obj.name,obj.flavor,obj.ingredients]]
        else:
            temp = self.dic[key]
            temp.append([obj.name,obj.flavor,obj.ingredients])
            self.dic[key] = temp
        self.total += 1

class White:
    def __init__(self,name,type = "White",flavor ="Plain",*args):
        self.name = name
        self.type = type
        self.flavor = flavor
        self.ingredients = args
    
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Flavor: {self.flavor}")
        print(f"Ingredients: {self.ingredients}")


class Dark:
    def __init__(self,name,type = "Dark",flavor ="Plain",*args):
        self.name = name
        self.type = type
        self.flavor = flavor
        self.ingredients = args
    
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Flavor: {self.flavor}")
        print(f"Ingredients: {self.ingredients}")



Choco = Chocolates()
print("*********************************************")
Choco.print_info()
print("1================================")
c1 = White("Dairy Milk")
c1.print_info()
print("2================================")
Choco.update_info(c1)
Choco.print_info()
print("3================================")
c2 = White("Hershey's","White", "Hazelnut","milk","sugar")
c2.print_info()
print("4================================")
Choco.update_info(c2)
Choco.print_info()
print("5================================")
c3 = Dark("Galaxy","Dark","Wafer")
c4 = Dark("Kitkat")
print("6================================")
c3.print_info()
print("7================================")
c4.print_info()
print("8================================")
Choco.update_info(c3)
Choco.update_info(c4)
print("9================================")
Choco.print_info()
print("10================================")
c5 = Dark("Dairy Milk", "Milk", "Plain","milk","sugar")
Choco.update_info(c5)
Choco.print_info()



