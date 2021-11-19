class Account:
    def __init__(self,name="Default Account",balance=0):
        self.name = name
        self.balance = float(balance)
    def details(self):
        print(self.name)
        return self.balance
    def withdraw(self,money):
        sum1 = self.balance - money
        sum1 = float(sum1)
        if sum1 >3070:
            print("Withdraw successful! New balance is:",sum1)
        else:
            print("Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")



a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)