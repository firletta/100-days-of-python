import turtle
import pandas
from state import State
from scoreboard import Scoreboard

SCREEN_WIDTH = 820
SCREEN_HEIGHT = 600
GAME_TITLE = "U.S. States Game"
BG_IMG = "blank_states_img.gif"
STATES_FILE = "50_states.csv"

STATES_DATA = pandas.read_csv(STATES_FILE)
STATE_NAMES = STATES_DATA['state'].to_list()

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.scoreboard = Scoreboard()
        self.setup_screen()
        self.guessed_states = []

    def setup_screen(self):
        """Set up the turtle screen."""
        self.screen.title(GAME_TITLE)
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgpic(BG_IMG)

    def state_exists(self, state_name):
        """Check if a state exists."""
        if state_name.rstrip().title() in STATE_NAMES:
            self.guessed_states.append(state_name.rstrip().title())
            return True
        return False

    def save_states_to_learn(self):
        """Save the states to learn to a CSV file."""
        states_to_learn = [state for state in STATE_NAMES if state not in self.guessed_states]
        states_to_learn_data_frame = pandas.DataFrame(states_to_learn, columns=['state'])
        states_to_learn_data_frame.to_csv('states_to_learn.csv', index=False)

    def game_over(self):
        """End the game and save the states to learn."""
        self.save_states_to_learn()
        # Add any other game over logic here

    def show_state_on_map(self, state_name):
        """Show a state on the map."""
        state_data = STATES_DATA[STATES_DATA['state'] == state_name]
        if not state_data.empty:
            x = state_data['x'].values[0]
            y = state_data['y'].values[0]
            state = State(state_name, (x, y))
        else:
            print(f"State '{state_name}' not found in the list of states.")

    def play(self):
        """Main game loop."""
        game_is_on = True
        prompt = "State's name:"
        while game_is_on:
            state_guess = self.screen.textinput(title=" Guess the State", prompt=prompt)
            if state_guess is None:
                self.save_states_to_learn()
                break
            state_guess = state_guess.title()
            if self.state_exists(state_guess):
                self.show_state_on_map(state_guess)
                self.scoreboard.update_scoreboard()
                prompt = "State's name:"
            else:
                prompt = "State not found. Try again:"
            if self.scoreboard.score == len(STATE_NAMES):
                game_is_on = False
                self.scoreboard.game_over()

        turtle.update()
        turtle.mainloop()

if __name__ == "__main__":
    game = Game()
    game.play()