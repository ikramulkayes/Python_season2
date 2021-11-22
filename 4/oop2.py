class Customer:
    def __init__(self,name=None):
        self.name = name
    def greet(self,name=None):
        if name != None:
            self.name = name
            print(f"Hello {self.name}!")
        else:
            print("Hello!")
    def purchase(self,*args):
        print(f"{self.name}, you purchased {len(args)} item(s):")
        for elm in args:
            print(elm)
    


customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")