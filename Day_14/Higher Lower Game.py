from Logo import *
from game_data import data
import random


def game():
    """Function to play the game"""
    print(logo)
    print("Welcome to Higher Lower Game")
    game_over = False

    def item_generation():
        """Random Instagram data generator"""
        for _ in range(0, len(data)):
            item = random.choice(data)
            return item

    def printing():
        """Printing items for comparison"""
        print("Which Instagram account has more followers?\n")
        print("1 -", item_1["name"], item_1["description"], item_1["country"])
        print(vs)
        print("2 -", item_2["name"], item_2["description"], item_2["country"])

    def compare():
        """Account followers comparison"""
        if item_1["follower_count"] > item_2["follower_count"]:
            return 1
        if item_2["follower_count"] > item_1["follower_count"]:
            return 2

    points = 0
    item_1 = item_generation()
    while not game_over:
        item_2 = item_generation()
        printing()
        user_reply = int(input("You reply is:\n"))
        if user_reply == compare():
            points += 1
            fixed_item = compare()
            print(f"You are right! Correct answer is {fixed_item}. "
                  f"Your points are:{points}")
            if fixed_item == 2:
                item_1 = item_2
        else:
            game_over = True
            print("Game over")
            print(f"Correct answer is {compare()}")
    print(f"Your final points are {points}")

    def play_again():
        """Function asks user to play again"""
        start_again_reply = input("Do you want to start the game "
                                  "again? Please type 'y' or 'n'").lower()
        if start_again_reply == 'y':
            game()
        else:
            print("Thank you for playing! Goodbye!")
            quit()
    play_again()

game()
