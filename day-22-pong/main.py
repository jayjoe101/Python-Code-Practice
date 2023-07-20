from turtle import Screen
from score import Score
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title('pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

scoreboard = Score()
l_paddle = Paddle('left')
r_paddle = Paddle('right')
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.paddle_up, 'Up')
screen.onkeypress(r_paddle.paddle_down, 'Down')
screen.onkeypress(l_paddle.paddle_up, 'w')
screen.onkeypress(l_paddle.paddle_down, 's')

game = True
speed = 3
while game:
    screen.update()
    time.sleep(0.01)
    ball.forward(speed)

    # detects wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect right paddle collision
    if ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        speed += .5
        ball.paddle_bounce()
    
    # dectect left paddle collision
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50:
        speed += .5
        ball.paddle_bounce()

    # detects if ball went past a paddle
    if ball.xcor() > 400:
        scoreboard.add_lscore()
        time.sleep(1)
        speed = 3
        ball.serve_ball()
    elif ball.xcor() < -400:
        scoreboard.add_rscore()
        time.sleep(1)
        speed = 3
        ball.serve_ball()
    
    # end game criteria 
    if scoreboard.rscore > 5 or scoreboard.lscore > 5:
        scoreboard.game_over()
        game = False


screen.exitonclick()