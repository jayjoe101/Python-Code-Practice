from turtle import Screen
import time
from traffic import Traffic
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.title('Crossy Road')
screen.bgcolor('grey')
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

player = Player()

screen.onkeypress(player.move_up, 'w')
screen.onkeypress(player.move_left, 'a')
screen.onkeypress(player.move_down, 's')
screen.onkeypress(player.move_right, 'd')
screen.listen()

player.set_position()
cars = Traffic()
level = Scoreboard()

speed = 1
gameison = True
levelison = True
while gameison:
    
    cars.create_traffic(level.level, speed)
    time.sleep(1)

    while levelison:
        time.sleep(.01)
        screen.update()

        if player.ycor() > 270:
            player.set_position()
            level.add_score()
            cars.clear_traffic()
            speed += 1
            break

        for c in cars.traffic:
            c.move()
            if c.xcor() < -320:
                c.car_position()

            if c.distance(player) < 22:
                gameison = False
                levelison = False


level.game_over()
screen.exitonclick()