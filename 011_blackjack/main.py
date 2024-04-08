############### Blackjack Project #####################

from art import logo
import random
import unicodedata


SUITS = ['♣️', '♦️', '♥️', '♠️']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = [rank + suit for suit in SUITS for rank in RANKS]

def main():

    print(logo)
    
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 21 or computer_score == 21 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'hit' to get another card, 'stand' to pass: ")
            if should_continue == 'hit':
                player_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 21 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if player_score > 21 or (computer_score <= 21 and computer_score > player_score):
        result = "You lose."
    elif player_score == computer_score:
        result = "It's a draw."
    else:
        result = "You win!"

    print(result)



def deal_card():
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_score(hand):
    values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    score = 0
    aces = 0

    for card in hand:
        rank = card[:-2]
        score += values[rank]
        if rank == 'A':
            aces += 1

    # If score is over 21 and there's an ace in hand, change its value from 11 to 1
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

if __name__ == "__main__":
    main()