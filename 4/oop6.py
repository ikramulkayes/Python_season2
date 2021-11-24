class Vehicle:
    def __init__(self):
        self.lst = [0,0]
    def moveUp(self):
        self.lst[1] += 1
    def moveDown(self):
        self.lst[1] -= 1
    def moveRight(self):
        self.lst[0] += 1
    def moveLeft(self):
        self.lst[0] -= 1
    def print_position(self):
        print(tuple(self.lst))


car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()