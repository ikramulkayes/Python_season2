
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

game_on_off = True
while game_on_off:
    snake.movesnake()
    screen.update()
    time.sleep(0.1)
    if snake.distancefromfood(food) < 15:
        food.refresh()
        snake.extendsnake()
        score.increase()
    if snake.distancefromwall():
        game_on_off = False
        score.gameover()
    if snake.hitwithtail():
        game_on_off = False
        score.gameover()




screen.exitonclick()

