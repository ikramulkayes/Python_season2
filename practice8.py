import turtle as t
timmy = t.Turtle()
screen = t.Screen()
screen.setup(width=500,height=400)
userbet = screen.textinput(title="Make Your bet!",prompt="which turtle gonna win!:")
colorlst = ["red","green","yellow","blue","brown","purple"]
timmy.penup()
count = 180
for i in colorlst:
    timmy = t.Turtle(shape="turtle")
    timmy.penup()
    timmy.color(i)
    timmy.goto(x=-230,y=count)
    count = count -60
screen.exitonclick()
