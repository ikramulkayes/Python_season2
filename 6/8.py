from math import pi
class Cylinder:
    radius = 5
    height = 18
    def __init__(self,nradius,nheight):
        print(f"Default radius={Cylinder.radius} and height={Cylinder.height}")
        print(f"Updated: radius={nradius} and height={nheight}")
        self.height = nheight
        self.radius = nradius
        Cylinder.radius = nradius
        Cylinder.height = nheight
    @classmethod
    def swap(cls,height,radius):
        obj = cls(radius,height)
        return obj
    @staticmethod
    def area(radius,height):
        sum1 = (2*pi*radius*radius) + (2*pi*radius*height)
        print(f"Area: {sum1}")
    @staticmethod
    def volume(radius,height):
        sum1 = pi*radius*radius*height
        print( f"Volume: {sum1}")
    @classmethod
    def changeFormat(cls,word):
        radius,height = word.split("-")
        obj = cls(float(radius),float(height))
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
    
    

    