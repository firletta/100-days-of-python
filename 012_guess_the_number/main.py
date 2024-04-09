from art import logo
import random

MAX_NUMBER = 100
ATTEMPS_EASY = 10
ATTEMPS_HARD = 5

def main():
    print(f"{logo}\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    answer = random.randint(1, MAX_NUMBER)
    attempts = ATTEMPS_EASY if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy" else ATTEMPS_HARD

    while attempts > 0:
        user_guess = int(input(f"\nYou have {attempts} attempts remaining to guess the number.\nMake a guess: "))

        if user_guess < answer:
            print("Too low.")
        elif user_guess > answer:
            print("Too high.")
        else:
            print("You got it!")
            break

        attempts -= 1

        if attempts > 0:
            print("Guess again.")
        else:
            print(f"You've run out of guesses, you lose.\nThe number was {answer}.")
            break
  
if __name__ == "__main__":
    main()