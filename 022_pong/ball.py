from turtle import Turtle

BALL_MOVE_INCREMENT = 3

class Ball(Turtle):
    """Represents a ball in the pong game."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.goto(0, 0)
        self.x_move = BALL_MOVE_INCREMENT
        self.y_move = BALL_MOVE_INCREMENT

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_paddle()