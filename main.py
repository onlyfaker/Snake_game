#todo/done - 1. create snake body
#todo/done - 2. move the snake
#todo/done - 3. control snake
#todo/done - 4. detect food collision
#todo/done - 5. create scoreboard
#todo/done - 6. wall collsion
#todo/done - 7. tail collsion


import time
import turtle
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #tracer is off

food = Food()
scoreboard = Scoreboard()
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    screen.update()
    snake.move()
    screen.update()

    # detect collsion with food
    if snake.head.distance(food) <= 18:
        scoreboard.score_count+=1
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    screen.update()
    #Detect collsion with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        game_on=False
    screen.update()

    # Detect collision with tail
    for segment in snake.segments:
        if snake.head==segment:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
