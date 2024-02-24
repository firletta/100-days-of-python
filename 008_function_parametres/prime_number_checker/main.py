import math

def main():
    number = int(input("Check this number: "))
    if prime_checker(number=number):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    
def prime_checker(number):
    if number == 1:
        return False
    return not any(number % i == 0 for i in range(2, math.isqrt(number) + 1))

if __name__ == "__main__":
    main()
