class ParcelKoro:
    def __init__(self,name = "No name set",weight=0):
        self.name = name
        self.product_weight = weight
        self.fee = 0
    def calculateFee(self,location=None):
        if location != None:
            charge = 100
        else:
            charge = 50
        if self.product_weight == 0:
            pass
        else:
            self.fee = (self.product_weight*20)+charge
    def printDetails(self):
        print("Customer Name:",self.name)
        print("Product Weight:",self.product_weight)
        print("Total fee:",self.fee)




print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()