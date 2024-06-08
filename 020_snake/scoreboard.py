from turtle import Turtle

SCORE_POSITION = (-285, 270)
FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 32, "normal")
FONT_COLOR = "white"
GAME_OVER_FONT_COLOR = "red"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(FONT_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(*SCORE_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write("Score: {}".format(self.score), align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        
        self.goto(0, 0)
        self.color(GAME_OVER_FONT_COLOR)
        self.write("Game Over", align="center", font=GAME_OVER_FONT)
