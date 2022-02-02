class Processor:
    def __init__(self, model, thread, core):
        self.model = model
        self.core = core
        self.thread = thread
    def getInfo(self):
        return "Model:"+self.model+ "\nCores:"+str(self.core)+ "\nThreads:"+ str(self.thread) 
# Write your code here

class Intel(Processor):
    def __init__(self, model, thread, core,price):
        super().__init__(model, core, thread)
        self.price = price
    def getInfo(self):
        print( super().getInfo())
        print(f"Price: {self.price} taka")
class AMD(Intel):
    def __init__(self, model, thread, core, price):
        super().__init__(model, thread, core, price)


      
p1 = Intel("Intel i5 10th Gen",6,12,17000)
p2 = AMD("Ryzen 5 3500X",6,6,13800)
p3 = AMD("Ryzen 5 3600",6,12,16900)
print('======================')
p1.getInfo()
print('======================')
p2.getInfo()
print('======================')
p3.getInfo()
