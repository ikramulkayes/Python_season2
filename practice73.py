from math import pi
class Cylinder:
    radius = 5
    height = 18
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
        print(f"Default radius={Cylinder.radius} and height={Cylinder.height}.")
        print(f"Updated: radius={self.radius} and height={self.height}.")
        Cylinder.radius = self.radius
        Cylinder.height = self.height
    @staticmethod
    def area(radius,height):
        area = 2*pi*radius*radius + 2*pi*radius*height
        print(f"Area: {area}")
    @staticmethod
    def volume(radius,height):
        volume = pi*radius*radius*height
        print(f"Volume: {volume}")
    @classmethod
    def swap(cls,height,radius):
        obj = Cylinder(radius,height)
        return obj
    @classmethod
    def changeFormat(cls,word):
        word = word.split("-")
        obj = Cylinder(int(word[0]),int(word[1]))
        return obj


c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)
