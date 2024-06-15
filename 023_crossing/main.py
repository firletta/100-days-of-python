import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SLEEP_TIME = 0.1

def game_loop(screen, player, scoreboard, car_manager):
    game_is_on = True
    while game_is_on:
        time.sleep(SLEEP_TIME)
        screen.update()
        car_manager.move_cars()
        if player.is_at_finish_line():
            player.go_to_start()
            scoreboard.increase_level()
            car_manager.level_up()
        if car_manager.check_collision(player):
            game_is_on = False
            scoreboard.game_over()

def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    
    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(player.go_up, "Up")

    game_loop(screen, player, scoreboard, car_manager)

    screen.exitonclick()

if __name__ == "__main__":
    main()