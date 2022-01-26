# Write you code here
class Dominos:
    def __init__(self,name):
        self.name = name
        print(f"Domino’s. The Pizza Delivery Experts.")
        self.dic = {}
        self.count = 0
    def addPizza(self,*args):
        for elm in args:
            k = ""
            if "Chicken" in elm.name:
                k = "Chicken"
            elif "Beef" in elm.name:
                k = "Beef"
            else:
                k = "Cheese"
            if k not in self.dic.keys():
                self.dic[k] = [[elm.name,elm.topings]]
            else:
                temp = self.dic[k]
                temp.append([elm.name,elm.topings])
                self.dic[k] = temp
            self.count += 1
    def showMenu(self):
        print(f"Total number of pizzas: {self.count}")
        for k,v in self.dic.items():
            print(f"{k} Pizza: {len(v)}")
            for elm in v:
                print(f"Name: {elm[0]}, Toppings: {elm[1]}")
    


class Pizza:
    def __init__(self,*args):
        self.name = args[0]
        if len(args)<2:
            print("A pizza without toppings cannot be created.")
        else:
            self.topings = list(args[1::])
    def setToppings(self,*args):
        print(f"Toppings added to {self.name} pizza.")
        self.topings = list(args)
    



#======================================================================
#Do not change the codes below
dom = Dominos("Domino's Pizza")
print("1.=================================")
p1 = Pizza("Spicy Chicken","Spicy Chicken","Onion","Capsicum")
dom.addPizza(p1)
p2 = Pizza("Margherita","Mozzarella Cheese")
print("2.=================================")
p3 = Pizza("Beef Kala Bhuna")
print("3.=================================")
p3.setToppings("Curried Beef","Capsicum","Paprika","Onion")
print("4.=================================")
dom.addPizza(p2,p3)
p4 = Pizza("Chicken Dominator","Barbecue Chicken,Spicy Chicken,Grilled Chicken")
p5 = Pizza("Beefzza","Minced Beef","Beef Pepperoni","Onion","Jalapeno")
dom.addPizza(p4,p5)
print("5.=================================")
dom.showMenu()
print("6.=================================")