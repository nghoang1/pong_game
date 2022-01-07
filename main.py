from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
scoreboard = ScoreBoard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.up)

screen.onkeypress(key="Down", fun=r_paddle.down)

screen.onkeypress(key="w", fun=l_paddle.up)

screen.onkeypress(key="s", fun=l_paddle.down)
game_one = True
while game_one:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball boucing
        ball.bounce_y()
        ball.move_speed *=0.9
    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()
screen.exitonclick()
