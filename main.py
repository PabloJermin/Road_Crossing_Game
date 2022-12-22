import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_m = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=player.go_up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_m.create_car()
    car_m.move_cars()

#     colision with car
    for car in car_m.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

#     sucessful crossing
    if player.sucess_cross():
        player.go_to_start()
        car_m.level_up()
        score.increase_lev()




screen.exitonclick()