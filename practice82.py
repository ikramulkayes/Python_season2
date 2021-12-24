class iceage():
    def show(self):
        print("Welcome to the iceage",end=" ")
class mammoth(iceage):
    def show(self):
        super().show()
        print("Hi this is manny")

obj = mammoth()
obj.show()


class genere():
    def display(self):
        print("There are many genre of books",end=" ")
class fiction(genere):
    def show(self):
        print("I like the fiction most",end=" ")
class mystery(fiction):
    def show(self):
        print("Whoa I love mystery",end=" ")
b = mystery()
b.show()
b.show()


class panda:
    def show(self):
        value = 20
        print(value)
class kungfu(panda):
    def disp(self):
        print(self.value)
p = kungfu()
p.disp()