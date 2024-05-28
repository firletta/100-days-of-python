from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()


def main():
    print(timmy)
    timmy.shape("turtle")
    timmy.color("aquamarine3")
    timmy.forward(100)

    print(my_screen.canvheight)
    my_screen.exitonclick()


if __name__ == "__main__":
    main()