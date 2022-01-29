class BFC:
    order_id = 80
    menu = {}
    def __init__(self) -> None:
        self.menu = {}
    def addChicken(self,*args):
        for elm in range(0,len(args),2):
            BFC.menu[args[elm]] = args[elm+1]
    def placeOrderof(self,obj):
        sum1 = 0
        BFC.order_id += 1
        print(f"Order ID: {BFC.order_id}")
        print(f"Customer name:{obj.name}")
        print("Order:")
        lst = obj.order.split(",")
        for elm in lst:
            count = elm[0]
            count = int(count)
            sum1 += count*BFC.menu[elm[2::]]
            print(f"Burger:{elm[2::]} , Quantity:{elm[0]}")
        obj.money = sum1
        


        

        

class Customer:
    def __init__(self,name):
        self.name = name
        self.order = None
        self.money = None
    def setOrder(self,gg):
        self.order = gg
    def __str__(self) -> str:
        return(f"Bill of {self.name} is {self.money} taka")
    







print(f"It's been a wonderful day! \nToday, we have already served {BFC.order_id} customers. Few more to go before we close for today.")
print("**************************************************")
outlet1 = BFC()
print("1.==========================================")
print("Chicken Menu:")
print(BFC.menu)
print("2.==========================================")
outlet1.addChicken('Regular',95,'Spicy',125)
print("3.==========================================")
print("Chicken Menu:")
print(BFC.menu)
print("4.==========================================")
c1 = Customer("Ariyan")
c1.order = "2xRegular"
outlet1.placeOrderof(c1)
print("5.==========================================")
c2 = Customer("Ayan")
c2.setOrder("2xRegular,3xSpicy")
print("6.==========================================")
outlet1.placeOrderof(c2)
print("7.==========================================")
print(c1)
print("8.==========================================")
print(c2)