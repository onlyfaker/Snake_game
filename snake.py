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
        self.current_direction = RIGHT  # Initial direction
        self.next_direction = RIGHT  # Direction to change to on next move
        self.is_turning = False  # Flag to prevent multiple turns per move cycle

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
        # Apply the next direction at the beginning of the move cycle
        if self.current_direction != self.next_direction:
            self.head.setheading(self.next_direction)
            self.current_direction = self.next_direction

        # Move the snake segments
        for seg in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg - 1].xcor()
            new_ycor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_xcor, new_ycor)

        self.head.forward(MOVE_DISTANCE)
        self.is_turning = False  # Reset turning flag after completing the move

    def up(self):
        # Only change direction if not going in the opposite direction
        if self.current_direction != DOWN and not self.is_turning:
            self.next_direction = UP
            self.is_turning = True

    def down(self):
        if self.current_direction != UP and not self.is_turning:
            self.next_direction = DOWN
            self.is_turning = True

    def left(self):
        if self.current_direction != RIGHT and not self.is_turning:
            self.next_direction = LEFT
            self.is_turning = True

    def right(self):
        if self.current_direction != LEFT and not self.is_turning:
            self.next_direction = RIGHT
            self.is_turning = True