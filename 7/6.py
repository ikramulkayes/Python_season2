class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base
    def get_height_base(self):
        return "Height: "+str(self.height)+",Base: "+str(self.base)
#write your code here

class triangle(Shape):
    def __init__(self, name='Default', height=0, base=0):
        super().__init__(name=name, height=height, base=base)
    def calcArea(self):
        self.area = 0.5*self.base*self.height
    def printDetail(self):
        print(f"Shape name: {self.name}")
        print(f"Height: {self.height}, Base: {self.base}")
        return f"Area: {self.area}"

class trapezoid(Shape):
    def __init__(self, name='Default', height=0, base=0,side_A=0):
        super().__init__(name=name, height=height, base=base)
        self.side_A = side_A
    def calcArea(self):
        self.area = 0.5*(self.base+self.side_A)*self.height
    
    def printDetail(self):
        print(f"Shape name: {self.name}")
        print(f"Height: {self.height}, Base: {self.base}, Side_A: {self.side_A}")
        return f"Area: {self.area}"




tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())