from turtle import Turtle

PADDLE_MOVE_INCREMENT = 5
SCREEN_BOUNDARY_Y = 250


class Paddle(Turtle):
    """Represents a paddle in the pong game."""

    def __init__(self, initial_x, initial_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(initial_x, initial_y)

    def move_up(self):
        new_y = self.ycor() + PADDLE_MOVE_INCREMENT
        if self._is_within_boundaries(new_y):
            self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - PADDLE_MOVE_INCREMENT
        if self._is_within_boundaries(new_y):
            self.sety(new_y)

    def _is_within_boundaries(self, y):
        return -SCREEN_BOUNDARY_Y <= y <= SCREEN_BOUNDARY_Y
