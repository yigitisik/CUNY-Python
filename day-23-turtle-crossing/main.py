import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#set up initial screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#initialize main objs
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#set up keyboard control
screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.move_left(), "Left")
screen.onkeypress(player.move_right(), "Right")

#game running and logic
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.move_cars()

    #detect turtle collision w/ car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect successful completion of level
    if player.is_player_at_finish_line():
        player.set_player_to_orig_pos()
        # increase game speed with level up
        car_manager.car_increase_level_speed()
        scoreboard.scoreboard_increase_level()

screen.exitonclick()

