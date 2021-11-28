class ShoppingCart:
    def __init__(self,name):
        self.sname = name
        self.cstring = ""
        self.totalcost = 0
        self.count = 0
    def addGadget(self,*args):
        for elm in range(0,len(args),2):
            
            stock = args[elm+1]
            if stock > args[elm].quant:
                print(f"{args[elm].name} stock is less than required quantity. Cannot add to cart.")
            else:
                self.count += 1
                self.cstring += f"Gadget:{args[elm].cat} Model:{args[elm].name} Price:{args[elm].price} Quantity:{stock} Stock:{args[elm].quant} pcs" +"\n"
                self.totalcost += args[elm].price *stock
    def printCartDetails(self):
        print(f"Details of {self.sname} cart:")
        self.cstring = self.cstring.rstrip("\n")
        print(f"Total gadgets in cart: {self.count}")
        print(self.cstring)
        print(f"Total cost of cart: {self.totalcost}$")





class Product:
    def __init__(self,name,catagory,price,quant = 0):
        self.name = name
        self.cat = catagory
        self.price = price
        self.quant = quant



s1 = ShoppingCart("Amazon")
p1 = Product("Razer BlackShark","Headset",99.99,5)
p2 = Product("Logitech G ProX Superlight","Mouse",150)
print("1.====================================")
s1.addGadget(p1,2,p2,1)
print("2.====================================")
p3 = Product("Razer Huntsman", "Keyboard", 249.99,12)
s1.addGadget(p3,1)
s1.addGadget(Product("HyperX Fury","Mousepad",26.99,1), 2)
print("3.====================================")
s1.printCartDetails()



    