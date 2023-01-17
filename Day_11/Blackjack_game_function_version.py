""" This is the program to play Blackjack game"""

from Blackjack_logo import *
import random


def deal_card():
    """Returns random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Returns sum of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and (11 in cards):
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Function compares the results and returns final result of the game"""
    if user_score > 21 and computer_score > 21:
        return "You lost!"
    if user_score == computer_score:
        return "It is draw!"
    elif computer_score == 0:
        return "Computer has blackjack. You lost!"
    elif user_score == 0:
        return "You have blackjack. You won!"
    elif user_score > 21:
        return "You lost! Your score is over 21"
    elif computer_score > 21:
        return "You won! Computer score is over 21"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lost!"


def game():
    """Initial game"""
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are:{user_cards} and current score:{user_score} ")
        print(f"Computer first card is:{computer_cards[0]} ")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
            print("Game over")
        else:
            user_reply = input("Type - 'hit' to get another card or "
                               "type -  'stand' to skip the round:\n").lower()
            if user_reply == "hit":
                user_cards.append(deal_card())
            if user_reply == "stand":
                compare(user_score, computer_score)
                game_over = True
        while computer_score < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

            print(f"Your final cards are:{user_cards} "
                  f"and final score:{user_score} ")
            print(f"Computer final cards are:{computer_cards} "
                  f"and final score:{computer_score} ")
            print(compare(user_score, computer_score))

    def start_again():
        """Function is asking the user if he wants to play again"""
        start_again_reply = input("Do you want to start the game again?"
                                  " Please type 'y' or 'n'").lower()
        if start_again_reply == 'y':
            game()
        else:
            print("Thank you for playing! Goodbye!")
            quit()
    start_again()
game()
