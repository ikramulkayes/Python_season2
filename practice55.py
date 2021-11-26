class Dominos:
    def __init__(self,name):
        self.name = name
        self.dic = {"Chicken Pizza":"","Beef Pizza":"","Cheese Pizza":""}
        self.ccount = 0
        self.bcount = 0
        self.cecount = 0
    def addPizza(self,*obj):
        for elm in obj:
            if elm.topings == None:
                print("A pizza without toppings cannot be created.")
            else:
                for k,v in self.dic.items():
                    m = k.split()
                    #print(m[0])
                    #print(elm.name.split())
                    if m[0] in elm.name.split():
                        self.dic[k] += f"Name:{elm.name}, Toppings: {elm.topings} \n" 
                        #print("YEYEYEYE")
                    elif m[0] == "Cheese":
                        #print("BABY")
                        self.dic[k] += f"Name:{elm.name}, Toppings: {elm.topings} \n" 


                                                      

    def showMenu(self):
        
        for k, v in self.dic.items():
            print(f"{k}:")
            print(v)
        #print(self.dic)
                    


        

class Pizza:
    def __init__(self,*args):
        args = list(args)
        self.name = args[0]
        if len(args)>1:
            self.topings = args[1::]
        else:
            self.topings = None
            print("A pizza without toppings cannot be added")
    def setToppings(self,*args):
        args = list(args)
        self.topings = args
        print(f"Topings added to {self.name}")


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
p4 = Pizza("Chicken Dominator","Barbecue Chicken,Spicy Chicken,Grilled  Chicken")
p5 = Pizza("Beefzza","Minced Beef","Beef Pepperoni","Onion","Jalapeno")
dom.addPizza(p4,p5)
print("5.=================================")
dom.showMenu()
print("6.=================================")
