
import turtle as t
import time
import os         #connected with practice10.py

path = 'F:\\Github\\Python_season2'
os.chdir(path)
from practice10 import Snake
screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")

while True:
    snake.movesnake()



screen.exitonclick()

