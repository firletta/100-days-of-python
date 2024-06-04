from turtle import Turtle, Screen, colormode
import random


def main():
    tim = Turtle()
    tim.shape("turtle")
    tim.color("white")
    
    draw_spirograph(tim, 120)

    screen = Screen()
    screen.exitonclick()


def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line(turtle):
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def random_hex_color():
    return "#" + "".join(random.choice('0123456789ABCDEF') for _ in range(6))

def draw_shape(turtle, num_sides):
    turtle.pencolor(random_hex_color())
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

def draw_shapes(turtle, num_shapes):
    for num_sides in range(3, num_shapes + 3):
        draw_shape(turtle, num_sides)


def random_walk(turtle, num_steps):
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.pensize(10)
    for _ in range(num_steps):
        turtle.pencolor(random_hex_color())
        turtle.setheading(random.choice([0, 90, 180, 270]))
        turtle.forward(30)

def draw_spirograph(turtle, num_circles):
    turtle.hideturtle()
    turtle.speed("fastest")
    angle = 360 / num_circles
    for _ in range(num_circles):
        turtle.pencolor(random_hex_color())
        turtle.circle(100)
        turtle.right(angle)

if __name__ == "__main__":
    main()