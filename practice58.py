class frodo:
    def __init__(self,x):
        self.x = x
    def __less__(self,other):
        if self.x < other.x:
            return False
        else:
            return True
a = frodo(10)
b = frodo(50)
print(a<b)