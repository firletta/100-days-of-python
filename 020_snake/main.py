from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SLEEP_TIME = 0.1
COLLISION_DISTANCE = 19


def main():
    """Main function to run the snake game."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    scoreboard = ScoreBoard()
    snake = Snake()
    food = Food()

    screen.listen()
    for direction, key in zip(snake.DIRECTIONS.keys(), ["Up", "Down", "Left", "Right"]):
        screen.onkey(
            lambda direction=direction: snake.change_direction(direction),
            key)
    for direction, key in zip(snake.DIRECTIONS.keys(), ["w", "s", "a", "d"]):
        screen.onkey(
            lambda direction=direction: snake.change_direction(direction),
            key)

    game_is_on = True
    while game_is_on:
        time.sleep(SLEEP_TIME)
        snake.move()
        screen.update()

        if snake.is_collision_with_food(food, COLLISION_DISTANCE):
            scoreboard.increase_score()
            snake.extend()
            food.refresh()

        if snake.is_collision_with_wall(
                SCREEN_WIDTH, SCREEN_HEIGHT) or snake.is_collision_with_tail():
            game_is_on = False
            scoreboard.game_over()

    screen.exitonclick()
    """Main function to run the snake game."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    scoreboard = ScoreBoard()
    snake = Snake()
    food = Food()

    screen.listen()
    for direction in snake.DIRECTIONS.keys():
        screen.onkey(
            lambda direction=direction: snake.enqueue_direction(direction),
            direction)

    game_is_on = True
    while game_is_on:
        time.sleep(SLEEP_TIME)
        snake.change_direction()
        snake.move()
        screen.update()

        if snake.is_collision_with_food(food, COLLISION_DISTANCE):
            scoreboard.increase_score()
            snake.extend()
            food.refresh()

        if snake.is_collision_with_wall(
                SCREEN_WIDTH, SCREEN_HEIGHT) or snake.is_collision_with_tail():
            game_is_on = False
            scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
