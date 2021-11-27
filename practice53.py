class Dominos:
    def __init__(self,name):
        self.name = name
        self.dic = {"Chicken Pizza":"","Beef Pizza":"","Cheese Pizza":"",}
    def addPizza(self,obj):
        if len(obj.topings) == 0:
             print("A pizza without toppings cannot be created.")
        else:   
            for elm in obj.lst:

                for k in self.dic.keys():
                    if k in elm:
                        self.dic[k] += elm + obj.topings
    def showMenu(self):
        print(self.dic)
                
                

class Pizza:
    def __init__(self,*args):
        self.lst = args
        self.tdic = []
        self.topings = []



    def addToppings(self,*args):
        self.topings = args
        for elm in self.lst:
            self.tdic[elm] = [args]



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
        
