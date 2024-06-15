from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_SHAPE = "turtle"
PLAYER_HEADING = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(PLAYER_SHAPE)
        self.penup()
        self.setheading(PLAYER_HEADING)
        self.go_to_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y