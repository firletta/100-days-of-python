from turtle import Turtle

class Snake:
    """A class representing a snake in a game."""

    COLOR = "light green"
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
                self.create_turtle(x=-self.STEP * i, y=0))

    def create_turtle(self, x, y):
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

    def extend(self):
        """Extend the snake by one turtle."""
        self.turtles.append(self.create_turtle(
            x=self.turtles[-1].xcor(), y=self.turtles[-1].ycor()))

    def is_collision_with_food(self, food, distance):
        return self.head.distance(food) < distance

    def is_collision_with_wall(self, screen_width, screen_height):
        """Check if the snake collided with the wall."""
        x = self.head.xcor()
        y = self.head.ycor()
        return x > screen_width / 2 or x < -screen_width / 2 or \
               y > screen_height / 2 or y < -screen_height / 2

    def is_collision_with_tail(self):
        """Check if the snake collided with its tail."""
        for turtle in self.turtles[1:]:
            if self.head.distance(turtle) < 10:
                return True
        return False

    def reset(self):
        for turtle in self.turtles:
            turtle.reset()
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]