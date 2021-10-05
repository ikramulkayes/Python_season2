from turtle import Turtle,Screen
timmy = Turtle()
screen = Screen()
count = 0
for i in range(50):
    if count % 2 == 0:
        timmy.penup()
        timmy.forward(10)
    else:
        timmy.pendown()
        timmy.forward(10)
    count += 1
screen.exitonclick()
