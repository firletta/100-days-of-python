from turtle import Turtle, Screen
import random

STARTING_POSITIONS = {
    'red': (-230, 100),
    'orange': (-230, 70),
    'yellow': (-230, 40),
    'green': (-230, 10),
    'blue': (-230, -20),
    'purple': (-230, -50)
}

FINISH_LINE_X = 230

def create_turtles(colors):
    turtles = {}
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(color)
        turtle.goto(STARTING_POSITIONS[color])
        turtles[color] = turtle
    return turtles

def race(turtles, colors):
    is_race_on = True
    winner = None
    while is_race_on:
        for color in colors:
            if turtles[color].xcor() > FINISH_LINE_X:
                winner = color
                is_race_on = False
                break
            else:
                turtles[color].forward(random.randint(1, 10))
    return winner

def main():
    screen = Screen()
    screen.setup(width=500, height=400)

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win? Enter a color: ({', '.join(colors)})")

    turtles = create_turtles(colors)

    winner = race(turtles, colors) if user_bet else None

    if winner:
        if winner == user_bet:
            print(f"Congratulations! You've won! The {winner} turtle is the winner.")
        else:
            print(f"Sorry, you've lost. The {winner} turtle is the winner.")

    screen.exitonclick()

if __name__ == "__main__":
    main()