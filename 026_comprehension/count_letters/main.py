

def count_letters(sentence):
    """ Count the number of letters in words in a sentence. Returns  a dictionary with a word as a key and the number of letters in the word as a value."""
    return {word: len(word) for word in sentence.split()}


def main():
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    print(count_letters(sentence))

if __name__ == "__main__":
    main()