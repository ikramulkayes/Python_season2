class A:
    def __init__(self):
        self.var = "Bonjur"
        self.change(self.var)
    def change(self,v):
        v = "Hello"
obj = A()
print(obj.var)
