class Calculator:
    def __init__(self,num1,sym,num2):
        self.num1 = num1
        self.num2 = num2
        self.sym = sym
        self.sum1 = 0
        print("Let’s Calculate!")
    def add(self):
        self.sum1 = self.num1 + self.num2
        return self.sum1
    def subtract(self):
        self.sum1 = self.num1 - self.num2
        return self.sum1
    def multiply(self):
        self.sum1 = self.num1 * self.num2
        return self.sum1
    def divide(self):
        self.sum1 = self.num1 / self.num2
        return self.sum1

num1 = int(input("Enter a number: "))
op = (input("Enter your opperator: "))
num2 = int(input("Enter another number: "))
obj1 = Calculator(num1,op,num2)

if op == "+":
    sum1 = obj1.add()
elif op == "-":
    sum1 = obj1.subtract()
elif op == "*":
    sum1 = obj1.multiply()
elif op == "/":
    sum1 = obj1.divide()
print(f"Value 1: {num1}")
print("Operator:",op)
print(f"Value 2: {num2}")
print("Result",sum1)

    