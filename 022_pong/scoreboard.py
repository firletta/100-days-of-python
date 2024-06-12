from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Futura", 52, "bold")
LEFT_SCORE_POSITION = (-60, 230)
RIGHT_SCORE_POSITION = (60, 230)

class Scoreboard(Turtle):
    """Represents the scoreboard in the pong game."""

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(LEFT_SCORE_POSITION)
        self.write(f"{self.score_left:02}", align=ALIGNMENT, font=FONT)
        self.goto(RIGHT_SCORE_POSITION)
        self.write(f"{self.score_right:02}", align=ALIGNMENT, font=FONT)

    def increment_left_score(self):
        self.score_left += 1
        self.update_scoreboard()

    def increment_right_score(self):
        self.score_right += 1
        self.update_scoreboard()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)