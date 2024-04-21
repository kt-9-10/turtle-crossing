import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

refresh_late = 0.1

game_is_on = True
while game_is_on:
    time.sleep(refresh_late)
    screen.update()
    car_manager.generate_car()
    car_manager.move()
    car_manager.destroy()

    if player.is_goal():
        player.set_start()
        refresh_late *= 0.9
        scoreboard.increment_level()

    if car_manager.check_collision(player):
        scoreboard.display_gameover()
        game_is_on = False

screen.exitonclick()
