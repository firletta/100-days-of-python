ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

def main():
    print(logo)
    restart = 'yes'
    while restart == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print(f"The {direction}d text is: {caesar(text=text, shift=shift, cipher_direction=direction)}")
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    print("Goodbye")


def caesar(text, shift, cipher_direction):
    shift = shift % len(ALPHABET)
    if cipher_direction == 'encode':
        shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    elif cipher_direction == 'decode':
        shifted_alphabet = ALPHABET[-shift:] + ALPHABET[:-shift]
    else:
        raise ValueError("Direction must be 'encode' or 'decode'")
    shift_map = {original: shifted for original, shifted in zip(ALPHABET, shifted_alphabet)}
    return ''.join(shift_map.get(letter, letter) for letter in text)

if __name__ == "__main__":
    main()