import turtle as t
import time
screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake")
lst = []
screen.tracer(0)

count = 0
for i in range(5):
    timmy = t.Turtle(shape="square")
    timmy.color("white")
    timmy.penup()
    timmy.goto(x=count,y=0)
    count = count - 20
    lst.append(timmy)
while True:
    screen.update() #update the screen
    time.sleep(0.1) #make delay
    for i in range(len(lst)-1,0,-1):
        new_x =lst[i-1].xcor()
        new_y = lst[i-1].ycor()
        lst[i].goto(new_x,new_y)
    

    def UP():
        lst[0].setheading(90)
    def DOWN():
        lst[0].setheading(270)
    def RIGHT():
        lst[0].setheading(0)
    def LEFT():
        lst[0].setheading(180)

    screen.listen()
    screen.onkey(UP,"w")
    screen.onkey(DOWN,"s")
    screen.onkey(RIGHT,"d")
    screen.onkey(LEFT,"a")
    lst[0].forward(20)






        

screen.exitonclick()