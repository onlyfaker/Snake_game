#todo/done - 1. create snake body
#todo - 2. move the snake
#todo - 3. control snake
#todo - 4. detect food collision
#todo - 5. create scoreboard
#todo - 6. wall collsion
#todo - 7. tail collsion
import time
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #tracer is off

segments = []
xcor = 0
for square in range(0,3):
    body = Turtle(shape='square')
    body.penup()
    body.color('white')
    body.goto(xcor, 0)
    xcor-=20
    segments.append(body)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments)-1,0,-1):
        new_xcor = segments[seg-1].xcor()
        new_ycor = segments[seg-1].ycor()
        segments[seg].goto(new_xcor,new_ycor)
    segments[0].forward(20)


screen.exitonclick()
