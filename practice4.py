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
timmy.pensize(10)
for i in range(200):
    timmy.color(rancolor())
    timmy.forward(40)
    timmy.setheading(random.choice(ran_dir)) #goes to all directions
