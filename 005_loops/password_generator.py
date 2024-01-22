import random
import string

def password_generator(nr_letters, nr_symbols, nr_numbers):
    password_list = []

    password_list += [random.choice(string.ascii_letters) for _ in range(nr_letters)]
    password_list += [random.choice(string.punctuation) for _ in range(nr_symbols)]
    password_list += [random.choice(string.digits) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    return ''.join(password_list)

def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input(f"How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password = password_generator(nr_letters, nr_symbols, nr_numbers)
    print(password)

if __name__ == "__main__":
    main()
