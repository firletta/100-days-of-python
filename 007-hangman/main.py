import random
from hangman_art import logo, stages
from hangman_words import word_list

def main():
    print(logo)

    chosen_word = random.choice(word_list)
    # print(f'Pssst, the solution is {chosen_word}.')

    display = ['_' for _ in chosen_word]
    lives = 6
    guessed_letters = set()

    while "_" in display and lives > 0:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        else:
            if guess in guessed_letters:
                print(f"You've already guessed \"{guess}\".")
                continue
            guessed_letters.add(guess)
            if guess in chosen_word:
                for letter_index, letter in enumerate(chosen_word):
                    if letter == guess:
                        display[letter_index] = guess
            else:
                lives -= 1
                print(f"\"{guess}\" is not in the word. You lose a life.")
            print(stages[lives])
            print(' '.join(display),"\n")
        
    print(f"You win!" if lives > 0 else f"You lose! The word was \"{chosen_word}\".")

if __name__ == "__main__":
    main()