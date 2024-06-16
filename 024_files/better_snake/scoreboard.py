from turtle import Turtle

SCORE_POSITION = (-285, 270)
FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 32, "normal")
FONT_COLOR = "white"
GAME_OVER_FONT_COLOR = "red"
INITIAL_SCORE = 0
HIGH_SCORE_FILE = "high_score.txt"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = INITIAL_SCORE
        self.color(FONT_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(*SCORE_POSITION)
        self.update_scoreboard()

    @property
    def high_score(self):
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())

    @high_score.setter
    def high_score(self, score):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = INITIAL_SCORE
        self.update_scoreboard()