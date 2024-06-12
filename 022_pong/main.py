import keyboard
from turtle import Screen
from net import Net
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_START_X = 350
PADDLE_START_Y = 0
RIGHT_PADDLE = "right_paddle"
LEFT_PADDLE = "left_paddle"
BALL_BOUNCE_WALL_THRESHOLD = 290
BALL_BOUNCE_PADDLE_THRESHOLD = 50
BALL_OUT_OF_BOUNDS = 390
WINNING_SCORE = 12

KEY_BINDINGS = {
    RIGHT_PADDLE: {
        'Up': 'move_up',
        'Down': 'move_down',
    },
    LEFT_PADDLE: {
        'w': 'move_up',
        's': 'move_down',
    }
}


def main():
    """Main function to set up and start the game."""
    screen = setup_screen()
    net = Net()
    paddles = {
        RIGHT_PADDLE: Paddle(PADDLE_START_X, PADDLE_START_Y),
        LEFT_PADDLE: Paddle(-PADDLE_START_X, PADDLE_START_Y)
    }
    ball = Ball()
    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        ball.move()
        handle_key_bindings(paddles)

        if abs(ball.ycor()) > BALL_BOUNCE_WALL_THRESHOLD:
            ball.bounce_wall()

        if (ball.distance(paddles[RIGHT_PADDLE]) < BALL_BOUNCE_PADDLE_THRESHOLD and ball.xcor() > 320) or \
            (ball.distance(paddles[LEFT_PADDLE]) < BALL_BOUNCE_PADDLE_THRESHOLD and ball.xcor() < -320):
            ball.bounce_paddle()

        if abs(ball.xcor()) > BALL_OUT_OF_BOUNDS:
            if ball.xcor() > 0:
                scoreboard.increment_left_score()
            else:
                scoreboard.increment_right_score()
            ball.reset_position()

        if scoreboard.score_left == WINNING_SCORE or scoreboard.score_right == WINNING_SCORE:
            game_is_on = False
            scoreboard.display_game_over()

        screen.update()

    screen.exitonclick()


def setup_screen():
    """Set up the game screen."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)
    return screen


def handle_key_bindings(paddles):
    """Handle the key bindings for the paddles."""
    for paddle_name, bindings in KEY_BINDINGS.items():
        for key, action in bindings.items():
            if keyboard.is_pressed(key):
                try:
                    getattr(paddles[paddle_name], action)()
                except AttributeError:
                    print(
                        f"Error: {paddle_name} does not have method {action}")


if __name__ == "__main__":
    main()
