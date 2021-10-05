from turtle import Turtle,Screen
timmy = Turtle()
screen = Screen()
count = 3
for elm in range(10):
    for i in range(count):
        k = 360 / count
        timmy.forward(100)
        timmy.right(k)
    
    count += 1