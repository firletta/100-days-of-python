from turtle import Turtle

class Scoreboard(Turtle):
    """Represents the scoreboard in the game."""
    
    SCOREBOARD_FONT = ("Courier", 24, "normal")
    SCOREBOARD_COLOR = "black"
    SCOREBOARD_POSITION = (-364, 256)
    STARTING_SCORE = 0

    def __init__(self):
        """
        Initialize a new scoreboard.

        The scoreboard starts with a score of 0.
        """
        super().__init__()
        self.color(self.SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.score = self.STARTING_SCORE
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard with the current score."""
        self.clear()
        self.goto(self.SCOREBOARD_POSITION)
        self.score += 1
        self.write(f"Score: {self.score}", align="left", font=self.SCOREBOARD_FONT)