#todo/done - 1. create snake body
#todo/done - 2. move the snake
#todo/done - 3. control snake
#todo - 4. detect food collision
#todo - 5. create scoreboard
#todo - 6. wall collsion
#todo - 7. tail collsion
import time
from turtle import Turtle,Screen
from snake import Snake
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #tracer is off

snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.update()



screen.exitonclick()
