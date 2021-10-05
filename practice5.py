import turtle
import random
timmy = turtle.Turtle()
screen = turtle.Screen()
#ran_colors = ["red","blue","green"]
ran_dir = [0,90,180,270]


turtle.colormode(255)

def rancolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
timmy.speed("fastest")


def gapingfunc(gap):
    for i in range(360//gap):
        timmy.color(rancolor())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+gap)
gapingfunc(3)