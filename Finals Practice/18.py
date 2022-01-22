# Design the Foodcart and Food class so that the following expected output is generated.
class Foodcart:
    def __init__(self,name=None):
        self.name = name
        self.dic = {}
    def addFood(self,*args):
        if self.name !=None:
            for elm in args:
                self.dic[elm.name] = [elm.shop,elm.price]
        else:
            print("Please set the cart name first.")
    def setCartName(self,name):
        self.name = name
    def printCartDetails(self):
        if self.name != None:
            print(f"Details of {self.name}:")
            print(f"Total Items: {len(self.dic)}")
            for k,v in self.dic.items():
                print(f"Food Info : {k}, Food Shop : {v[0]}, Food Price : {v[1]}")
        else:
            print("Please set the cart name first.")
    def removeFood(self,name):
        if name not in self.dic.keys():
            print(f"{name} not found!")
        else:
            del self.dic[name]
            print(f"{name} removed from cart!")        

class Food:
    def __init__(self,name,shop,price):
        self.name = name
        self.shop = shop
        self.price = price
    def detail(self):
        print(f"Food Info : {self.name}, Food Shop : {self.shop}, Food Price : {self.price}")
    



#========================================================================================
# Do not change the codes below
cart1 = Foodcart()
food1 = Food('Burger','Chillox',180)
food2 = Food('Cake','Mr. Baker',1000)
print("===========================")
food1.detail()
print("===========================")
cart1.addFood(food1,food2)
print("===========================")
cart1.setCartName("Foodpanda")
cart1.addFood(food1,food2)
cart1.addFood(Food('Steak','Woodhouse Grill',2000))
print("===========================")
cart1.printCartDetails()
print("===========================")
cart1.removeFood("French Fry")
print("===========================")
cart1.removeFood("Steak")
print("===========================")
cart1.printCartDetails()