from turtle import Turtle

class State(Turtle):
    """Represents a state on the map."""
    
    STATE_FONT = ("Courier", 10, "normal")
    STATE_COLOR = "black"

    def __init__(self, name, position):
        """
        Initialize a new state.

        Args:
        name (str): The name of the state.
        position (tuple): The position of the state on the map.
        """
        super().__init__()
        self.color(self.STATE_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"{name}", align="left", font=self.STATE_FONT)