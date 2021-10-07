import turtle as t
import time                  #connected with practice11.py
screen = t.Screen()
class Snake:
    def __init__(self):
        self.lst = []
        self.createsnake()

    def createsnake(self):
        count = 0
        for i in range(5):
            timmy = t.Turtle(shape="square")
            timmy.color("white")
            timmy.penup()
            timmy.goto(x=count,y=0)
            count = count - 20
            self.lst.append(timmy)
    def movesnake(self):
        
            screen.update() #update the screen
            time.sleep(0.1) #make delay
            for i in range(len(self.lst)-1,0,-1):
                new_x =self.lst[i-1].xcor()
                new_y = self.lst[i-1].ycor()
                self.lst[i].goto(new_x,new_y)
            self.lst[0].forward(20)
            #self.lst[0].right(90)
    def up(self):
        if self.lst[0].heading() != 270:
            self.lst[0].setheading(90)
    def down(self):
        if self.lst[0].heading() != 90:
            self.lst[0].setheading(270)
    def right(self):
        if self.lst[0].heading() != 180:
            self.lst[0].setheading(0)
    def left(self):
        if self.lst[0].heading() != 0:
            self.lst[0].setheading(180)
    
