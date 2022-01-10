class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)

class ComplexNumber(RealNumber):
    def __init__(self, number=0,complex=0):
        super().__init__(number=(number))
        
        self.complex = (complex)
        try:
            if (self.number) > 0:
                pass
            else:
                pass
            if self.complex >0:
                self.symbolc = "+"
            else:
                self.symbolc = "-"
        except:
            self.number = number.number
            if (self.number) > 0:
                pass
            else:
                pass
            if self.complex >0:
                self.symbolc = "+"
            else:
                self.symbolc = "-"

    def __add__(self, anotherRealNumber):
        real = self.number +anotherRealNumber.number
        complex = self.complex+anotherRealNumber.complex
        obj = ComplexNumber(real,complex)
        return obj
    def __sub__(self, anotherRealNumber):
        real = self.number -anotherRealNumber.number
        complex = self.complex-anotherRealNumber.complex
        obj = ComplexNumber(real,complex)
        return obj
    def __str__(self):
        if self.symbolc == "+":
            return f"{self.number} {self.symbolc} {self.complex}i"
        else:
            return f"{self.number} {self.symbolc} {str(self.complex)[1::]}i"
    



r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)