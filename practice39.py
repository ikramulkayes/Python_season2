class Foodcart:
    def __init__(self):
        self.dic = {}
        self.cname = None
    def addFood(self,*args):
        if self.cname != None:
            for elm in args:
                self.dic[elm.item] = f"Food Shop: {elm.shop}, Food Price: {elm.price}"
        else:
            print("Please set the cart name first")
    def printCartDetails(self):
        print(f"Details of {self.cname}:")
        print(f"Total items: {len(self.dic)}")
        for k,v in self.dic.items():
            print("Food Info: "+k+", "+str(v))
    def removeFood(self,name):
        if name in self.dic.keys():
            del self.dic[name]
            print(f"{name} removed from cart!")
        else:
            print(f"{name} not found!")
    def setCartName(self,name):
        self.cname = name




class Food:
    def __init__(self,item,shop,price):
        self.item = item
        self.shop = shop
        self.price = price
    def detail(self):
        print(f"Food info: {self.item} Food Shop: {self.shop}, Food Price: {self.price}")




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
    