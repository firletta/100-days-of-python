from turtle import Turtle

SCOREBOARD_FONT = ("Courier", 24, "normal")
SCOREBOARD_COLOR = "black"
SCOREBOARD_POSITION = (-280, 260)
GAME_OVER_MESSAGE = "GAME OVER"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Level: {self.level}", align="left", font=SCOREBOARD_FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(GAME_OVER_MESSAGE, align="center", font=SCOREBOARD_FONT)