import time
from player import Player
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

game_on = True


def pause():
    global game_on
    if game_on:
        stop()
    else:
        game_on = True
        play()


def stop():
    global game_on
    game_on = False
    screen.exitonclick()


def game_over():
    scoreboard.game_over()
    stop()


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkey(pause, "Escape")


def play():

    num_update = 0
    n = 6

    while game_on:
        time.sleep(0.1)
        car_manager.move()
        screen.update()
        num_update += 1

        # detect turtle crossing
        if player.ycor() > 240:
            # increase score
            scoreboard.increase_score()
            # move back to starting position
            player.goto(STARTING_POSITION[0], STARTING_POSITION[1])
            # increase car speed
            car_manager.increase_speed()
            # increase frequency of new cars based on player score
            if n > 0 and scoreboard.level > 2 and scoreboard.level % 2 == 0:
                n -= 1

        # detect collision with car
        for car in car_manager.cars:
            if player.distance(car) < 20:
                game_over()

        # add more cars every n'th update
        if num_update > n and num_update % n == 0:
            car_manager.add_car()


play()
