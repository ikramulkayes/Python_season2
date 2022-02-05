class AppleProduct:
  def __init__(self, name, model, base_price):
    self.name = name
    self.model = model
    self.base_price = base_price
  def companyInfo(self):
    st = ("Company Name: Apple\nFouder: Steve Jobs, Steve Wozniak, Ronald Wayne\nCurrent CEO: Tim Cook\nAddress: Apple Inc, 2511 Laguna Blvd, Elk Grove, CA 95758, United States")    
    return st
  def feature(self):
    st = (f"Name: {self.name}\nProduct Model: {self.model}\nHardware Quality: Excellent Hardwares\nGuarantee/ Warranty: Apple Care")
    return st
  def __str__(self):
    print('This is apple product.')
  def calculatePrice(self):
    print('Total Price:', self.base_price)
  def __add__(self,other):
    sum1 = self.totalprice + other.totalprice
    return sum1  
# Write your codes here.
# Do not change the following lines of code.

class MacBookPro2020(AppleProduct):
    def __init__(self, name, model, ram,chip,tax):
        super().__init__(name, model, base_price = 1299)
        self.ram = ram
        self.chip = chip
        self.tax = tax
    def __str__(self):
        print("Product Details:")
        print(f"Name: {self.name}")
        print(f"Product Model: {self.model}")
        print("Hardware Quality: Excellent Hardwares")
        print(f"Guarantee/ Warranty: Apple Care")
        print(f"RAM: {self.ram}GB")
        print(f"Chip: {self.chip}")
        return(super().companyInfo())
    def calculatePrice(self):
        print("Calculating Total Price:")
        print(f"Base Price: {self.base_price}")
        print(f"Tax: {self.tax}%")
        print(f"Total Price: {self.base_price+self.base_price*(self.tax/100)}")
        self.totalprice = self.base_price+self.base_price*(self.tax/100)
    def __add__(self,other):
        sum1 = self.totalprice + other.totalprice
        return(sum1)

class iPhone12(MacBookPro2020):
    def __init__(self, name, model, ram, chip, tax):
        super().__init__(name, model, ram, chip, tax)
        self.base_price = 799


m1 = MacBookPro2020('MacBook', 'MacBookPro2020', 8, 'M1', 10)
print(m1)
print('====================================')
m1.calculatePrice()
print('###################################')
iphone = iPhone12('iPhone', 'iPhone 12', 8, 'A14', 5)
print(iphone)
print('====================================')
iphone.calculatePrice()  
print('###################################')
print('Total Price of these two products: ',end='')
print('%.2f Dollars'%(m1 + iphone))