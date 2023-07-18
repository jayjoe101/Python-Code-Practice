from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('black')

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def main():
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move_forward()

        # collided with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            game_on = False

        #collide with tail
        for s in snake.snake:
            if s == snake.head:
                pass
            elif snake.head.distance(s) < 10:
                scoreboard.game_over()
                game_on = False

        # collided with food
        if snake.head.distance(food) < 15:
            food.respawn()
            scoreboard.add_score()
            snake.add_snake()


screen.onkeypress(snake.move_up, 'w')
screen.onkeypress(snake.move_left, 'a')
screen.onkeypress(snake.move_down, 's')
screen.onkeypress(snake.move_right, 'd')
screen.listen()

main()

screen.exitonclick()
