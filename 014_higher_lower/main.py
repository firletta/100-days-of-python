import random
import os
from game_data import data
from art import logo, vs


def main():
    gameover = False
    score = 0
    while True:
        os.system('clear')
        print(logo)
        a = random.choice(data)
        data.remove(a)
        b = random.choice(data)
        data.append(a)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        answer = 'a' if a['follower_count'] > b['follower_count'] else 'b'
        if guess == answer:
            score += 1
            continue
        else:
            os.system('clear')
            print(f"Sorry, that's wrong. Final score: {score}")
            again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
            if again == 'yes':
                score = 0
                continue
            else:
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()