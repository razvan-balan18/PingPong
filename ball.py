from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 2.5
        self.y_move = 2.5
        self.move_speed = 0.01

    def create_ball(self):
        self.penup()
        self.color("white")
        self.shape("circle")

    def move_ball(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.7

    def paddle_hit(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
