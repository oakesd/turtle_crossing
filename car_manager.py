from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


def get_random_x():
    return random.randint(0, 280)


def get_random_y():
    return random.randrange(-220, 240, 20)


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        for _ in range(12):
            new_car = CarManager.Car(self.move_distance)
            new_car.goto(get_random_x(), get_random_y())
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.move()

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def add_car(self):
        new_car = CarManager.Car(self.move_distance)
        new_car.goto(280, get_random_y())
        self.cars.append(new_car)

    class Car(Turtle):

        def __init__(self, move_distance):
            super().__init__()
            self.move_distance = move_distance
            color = random.choice(COLORS)
            self.color(color)
            self.shape("square")
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.pu()

        def move(self):
            new_x = self.xcor() - self.move_distance
            self.goto(new_x, self.ycor())
