from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    
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
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def left(self):
        self.segments[0].setheading(180)
    def right(self):
        self.segments[0].setheading(0)



