from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

#   Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_from_wall()

#   Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_from_paddle()
        ball.x_move += 2
        ball.y_move += 2

#   Paddle misses the ball
    # for right
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.l_point()
        ball.x_move = 10
        ball.y_move = 10

    # for left
    if ball.xcor() < -410:
        scoreboard.r_point()
        ball.reset_position()
        ball.x_move = 10
        ball.y_move = 10


screen.exitonclick()
