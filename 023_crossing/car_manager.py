from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_CARS_NUMBER = 16
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
GRID_POSITIONS = [(x, y) for x in range(-250, 250, 50) for y in range(-200, 300, 50)]


class Car(Turtle):

    def __init__(self, position):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(position)
        self.set_direction()
        self.move()

    def set_direction(self):
        if self.ycor() % 100 == 0:
            self.setheading(0)
        else:
            self.setheading(180)

    def move(self):
        self.forward(self.move_distance)

    def check_and_reset(self):
        if self.xcor() > 300:
            self.goto(-300, self.ycor())
        elif self.xcor() < -300:
            self.goto(300, self.ycor())

    def check_collision(self, player):
        if self.distance(player) < 20:
            return True
        else:
            return False

class CarManager:

    def __init__(self):
        self.cars = []
        self.create_cars()

    def create_cars(self):
        random.shuffle(GRID_POSITIONS)
        self.cars = [Car(GRID_POSITIONS[i]) for i in range(STARTING_CARS_NUMBER)]

    def move_cars(self):
        for car in self.cars:
            car.move()
            car.check_and_reset()

    def increase_speed(self):
        for car in self.cars:
            car.move_distance += MOVE_INCREMENT

    def level_up(self):
        random.shuffle(GRID_POSITIONS)
        for i, car in enumerate(self.cars):
            car.goto(GRID_POSITIONS[i])
            car.set_direction()
        self.increase_speed()
        self.move_cars()

    def check_collision(self, player):
        for car in self.cars:
            if car.check_collision(player):
                return True
        return False