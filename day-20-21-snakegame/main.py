from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def main():
    while True:
        screen.update()
        time.sleep(0.05)
        snake.move_forward()

        # collided with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            time.sleep(.5)
            snake.reset()

        #collide with tail
        for s in snake.snake:
            if s == snake.head:
                pass
            elif snake.head.distance(s) < 10:
                scoreboard.game_over()
                time.sleep(.5)
                snake.reset()

        # collided with food
        if snake.head.distance(food) < 15:
            food.respawn()
            scoreboard.add_score()
            snake.add_snake()

        screen.update()

screen.onkeypress(snake.move_up, 'w')
screen.onkeypress(snake.move_left, 'a')
screen.onkeypress(snake.move_down, 's')
screen.onkeypress(snake.move_right, 'd')
screen.listen()

main()

screen.exitonclick()