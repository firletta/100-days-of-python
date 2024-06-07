from turtle import Screen
from snake import Snake
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SLEEP_TIME = 0.1


def main():
    """Main function to run the snake game."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()

    screen.listen()
    for direction in snake.DIRECTIONS.keys():
        screen.onkey(
            lambda direction=direction: snake.change_direction(direction),
            direction)

    game_is_on = True
    while game_is_on:
        time.sleep(SLEEP_TIME)
        snake.move()
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
