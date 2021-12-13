from math import pi
class Circle:
    def __init__(self,radius = 0):
        self.__radius = radius
    
    def setRadius(self,radius):
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius
    def area(self):
        return pi*self.__radius*self.__radius
    def __add__(self,other):
        obj = Circle()
        obj.setRadius(self.getRadius()+other.getRadius())
        return obj

c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())
    