import os
from art import logo

def main():
    print(logo)
    print("Welcome to the secret auction program.")
    bids = {}
    bidding_finished = False

    while not bidding_finished:
        name = input("What is your name?: ")
        price = int(input("What's your bid?: $"))
        bids[name] = price
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if should_continue == "no":
            bidding_finished = True
        elif should_continue == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
    print(highest_bidder(bids))

def highest_bidder(bids):
    winner = max(bids, key=bids.get)
    return f"The winner is {winner} with a bid of ${bids[winner]}"

if __name__ == "__main__":
    main()