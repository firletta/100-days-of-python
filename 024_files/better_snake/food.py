from turtle import Turtle
from random import randint

FOOD_SHAPE = "square"
FOOD_COLOR = "light coral"
FOOD_SPEED = "fastest"
GRID_SIZE = 20
GRID_RANGE = (-13, 13)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.color(FOOD_COLOR)
        self.speed(FOOD_SPEED)
        self.refresh()

    def refresh(self):
        x = randint(*GRID_RANGE) * GRID_SIZE
        y = randint(*GRID_RANGE) * GRID_SIZE
        self.goto(x, y)
