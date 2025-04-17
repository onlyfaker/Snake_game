from turtle import Turtle
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        xcor = 0
        for square in range(0, 3):
            body = Turtle(shape='square')
            body.penup()
            body.color('white')
            body.goto(xcor, 0)
            xcor -= 20
            self.segments.append(body)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_xcor = self.segments[seg-1].xcor()
            new_ycor = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_xcor,new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):#TODO - FIX; if I press in the same time UP and RIGHT or LEFT it can go into reverse(its hte same for rest)
        if self.head.heading() != DOWN:
                self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



