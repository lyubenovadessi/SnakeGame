from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_DOWN = 270
MOVE_LEFT = 180
MOVE_RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        snake = Turtle(shape="square")
        snake.color("purple")
        snake.penup()
        snake.goto(position)
        self.snake_segments.append(snake)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def snake_move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            seg_x = self.snake_segments[segment - 1].xcor()
            seg_y= self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(seg_x, seg_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)

    def move_down(self):
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)

    def move_left(self):
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT)

    def move_right(self):
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)


