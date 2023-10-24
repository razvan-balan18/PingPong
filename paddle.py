from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.build_paddle(direction)

    def build_paddle(self, direction):
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4.5, stretch_len=1)
        self.goto(direction)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
