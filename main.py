from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PingPong")
screen.listen()
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle1.move_down, "Down")
screen.onkeypress(paddle2.move_up, "w")
screen.onkeypress(paddle2.move_down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.move_ball()
    if ball.xcor() > 360 or ball.xcor() < -360:
        ball.game_over()
        game_on = False
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle1) < 50 and ball.xcor() > 340:
        ball.paddle_hit()
        score.increment_r()
    elif ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.paddle_hit()
        score.increment_l()

    screen.update()


screen.exitonclick()
