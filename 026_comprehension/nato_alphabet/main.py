import pandas

def load_nato_alphabet_dict():
    """Load the NATO alphabet from a CSV file into a dictionary."""
    nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
    return {row.letter: row.code for (_, row) in nato_alphabet.iterrows()}

NATO_ALPHABET_DICT = load_nato_alphabet_dict()

def create_phonetic_list(word):
    """Create a list of phonetic code words from a word."""
    phonetic_list = []
    for letter in word:
        if letter.upper() in NATO_ALPHABET_DICT:
            phonetic_list.append(NATO_ALPHABET_DICT[letter.upper()])
        else:
            print(f"Error: \"{letter}\" is not a supported letter.\nPlease enter only English alphabet letters.")
            return []
    return phonetic_list

def main():
    user_word = input("Enter a word: ")
    phonetic_list = create_phonetic_list(user_word)
    if phonetic_list:
        print(phonetic_list)

if __name__ == "__main__":
    main()