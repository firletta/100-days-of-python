import colorgram
from turtle import Turtle, Screen
import random


def main():
    screen = Screen()
    screen.colormode(255)
    hirst = Turtle()
    hirst.hideturtle()
    hirst.speed("fastest")
    hirst.penup()

    colors = extract_colors("image.jpg")

    start_pos = -225.00
    step_size = 50
    grid_size = 10
    dot_size = 20

    for row in range(grid_size):
        hirst.setposition((start_pos, start_pos + row * step_size))
        for _ in range(grid_size):
            hirst.pencolor(random.choice(colors))
            hirst.dot(dot_size)
            hirst.forward(step_size)

    screen.exitonclick()


def extract_colors(image_path):
    colors = colorgram.extract(image_path, 12)
    return [tuple(color.rgb) for color in colors]


if __name__ == "__main__":
    main()
