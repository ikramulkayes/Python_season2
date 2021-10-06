import turtle as t
timmy = t.Turtle()
screen = t.Screen()
def move_forward():
    timmy.forward(20)
def backwars():
    timmy.backward(20)

def counter_clock():
    new = timmy.heading() + 20
    timmy.setheading(new)
def clock():
    new = timmy.heading() - 20
    timmy.setheading(new)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=backwars)
screen.onkey(key="a",fun=counter_clock)
screen.onkey(key="d",fun=clock)
screen.onkey(key="c",fun=clear)
screen.exitonclick()