
import turtle as t
import time
import os         #connected with practice10.py

path = 'F:\\Github\\Python_season2'
os.chdir(path)
from practice10 import Snake
from practice13 import Food
from practice14 import Score
screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")


while True:
    snake.movesnake()
    screen.update()
    time.sleep(0.1)
    if snake.distancefromfood(food) < 15:
        food.refresh()
        score.increase()




screen.exitonclick()

