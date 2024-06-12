from turtle import Turtle

# Constants
NET_LENGTH = 20
NET_SEGMENT_LENGTH = 20
NET_START_Y = 300
NET_HEADING = 270
NET_WIDTH = 8

class Net(Turtle):
    """Class to represent the net in the middle of the pong game."""

    def __init__(self):
        """Initialize the net."""
        super().__init__()
        self.color("midnight blue")
        self.pensize(NET_WIDTH)
        self.penup()
        self.hideturtle()
        self.draw_net()

    def draw_net(self):
        """Draw the net on the screen."""
        self.goto(0, NET_START_Y)
        self.setheading(NET_HEADING)
        for _ in range(NET_LENGTH):
            self.pendown()
            self.forward(NET_SEGMENT_LENGTH)
            self.penup()
            self.forward(NET_SEGMENT_LENGTH)