class Coordinates:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y
    def detail(self):
        return (self.__x,self.__y)
    def setxcord(self,x):
        self.__x = x
    def setycord(self,y):
        self.__y = y
    def __add__(self,other):
        obj = Coordinates()
        obj.setxcord(self.__x +  other.__x)
        obj.setycord(self.__y + other.__y)
        return obj
    def __sub__(self,other):
        obj = Coordinates()
        obj.setxcord(self.__x -  other.__x)
        obj.setycord(self.__y - other.__y)
        return obj
    def __mul__(self,other):
        obj = Coordinates()
        obj.setxcord(self.__x *  other.__x)
        obj.setycord(self.__y * other.__y)
        return obj
    def __eq__(self,other):
        if self.__x == other.__x and self.__y == other.__y:
            return "The calculated coordinates are the same."
        else:
            return "The calculated coordinates are NOT the same."


p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))
p4 = p1 - p2
print(p4.detail())
p5 = p1 * p2
print(p5.detail())
point_check = (p4 == p5)
print(point_check)

    
