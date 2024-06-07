from turtle import Turtle


class Snake:
    """A class representing a snake in a game."""

    COLOR = "pale green"
    SHAPE = "square"
    STARTING_LENGTH = 3
    STEP = 20
    DIRECTIONS = {"Up": 90, "Down": 270, "Left": 180, "Right": 0}
    OPPOSITE_DIRECTIONS = {"Up": 270, "Down": 90, "Left": 0, "Right": 180}

    def __init__(self):
        """Initialize the snake."""
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def move(self):
        """Move the snake forward by one step."""
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].xcor(),
                                 self.turtles[i - 1].ycor())
        self.head.forward(self.STEP)

    def create_snake(self):
        """Create the initial snake."""
        for i in range(self.STARTING_LENGTH):
            self.turtles.append(
                self._create_turtle(x=-self.STEP * i, y=0))

    def _create_turtle(self, x, y):
        """Create a turtle at the given coordinates."""
        turtle = Turtle()
        turtle.shape(self.SHAPE)
        turtle.color(self.COLOR)
        turtle.penup()
        turtle.goto(x=x, y=y)
        return turtle

    def change_direction(self, direction):
        """Change the direction of the snake's movement."""
        if self.head.heading() != self.OPPOSITE_DIRECTIONS[direction]:
            self.head.setheading(self.DIRECTIONS[direction])
