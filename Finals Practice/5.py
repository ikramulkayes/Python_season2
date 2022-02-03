# Do not change the following lines of code.
class Fruit:
    Total_order=0
    
    def __init__(self, Order_ID, weight):
        self.Order_ID=Order_ID
        self.weight=weight
        Fruit.Total_order=Fruit.Total_order+1
    
    def __str__(self):
        return self.Order_ID+", Weight: "+str(self.weight)

class Mango(Fruit):
    def __init__(self, Order_ID, weight,variety,unit):
        super().__init__(Order_ID, weight)
        self.variety = variety
        self.unit = unit

    def __str__(self):
        k = super().__str__()
        return(k+ f" Variety: {self.variety} Total price: {self.weight*self.unit}")
    
    def __add__(self,other):
        sum1 = self.weight*self.unit
        sum2 = other.weight*other.unit
        return f"The total Price of the orders are: {sum1+sum2}"
    



class JackFruit(Fruit):
    def __init__(self, Order_ID, weight,unit):
        super().__init__(Order_ID, weight)
        
        self.unit = unit

    def __str__(self):
        k = super().__str__()
        return(k+ f" Totalprice: {self.weight*self.unit}")
    
    def __add__(self,other):
        sum1 = self.weight*self.unit
        sum2 = other.weight*other.unit
        return f"The total Price of the orders are: {sum1+sum2}"

    
m1=Mango("Order Id 1", 5,"GopalVog",250)
print(m1)
m2=Mango("Order Id 2", 5,"HariVanga", 230)
print(m2) 
j1=JackFruit("Order Id 3", 5,250)
print(j1)
j2=JackFruit("Order Id 4", 4,210)
print(j2)
print("Total number of Orders: "+str(Fruit.Total_order))
print("==================")
print(m1+m2)
print("==================")
print(j1+j2)
