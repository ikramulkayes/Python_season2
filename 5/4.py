class Color:
    def __init__(self,clr = None):
        self.clr =  clr
    
    def __add__(self,other):
        obj = Color()
        if self.clr == "red" and other.clr == "yellow":
            obj.clr = "Orange"
        elif self.clr == "yellow" and other.clr == "red":
            obj.clr =  "Orange"       
            
        elif self.clr == "red" and other.clr == "blue":
            obj.clr =  "Violet"
        elif self.clr == "blue" and other.clr == "red":
            obj.clr =  "Violet"
        elif self.clr == "yellow" and other.clr == "blue":
            obj.clr =  "Green"
        elif self.clr == "blue" and other.clr == "yellow":
            obj.clr =  "Green"
        return obj


C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)


