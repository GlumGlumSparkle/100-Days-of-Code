from guessing_game_logo import *
import random


def game():
    """Function starts the game"""
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    user_difficulty = input("Choose difficulty. Type 'easy' or 'hard'\n")
    game_over = False

    """Number generation"""
    generated_number = random.randint(1, 101)
    print(generated_number)

    def difficulty():
        """ Function sets up the difficulty in accordance to user choice"""
        if user_difficulty == "easy":
            attempts = 10
            return attempts
        if user_difficulty == "hard":
            attempts = 5
            return attempts

    def compare():
        """Function compares number chosen by user against generated number"""
        if user_number == generated_number:
            return True
        if user_number > generated_number:
            return f"Too high"
        if user_number < generated_number:
            return f"Too low"

    print(f"You have {difficulty()} attempts remaining to guess the number\n")
    attempts_left = difficulty()

    while not game_over:
        """Code counts user attempts and asks user for number input"""
        if attempts_left != 0:
            while difficulty() <= attempts_left > 0:
                user_number = int(input("Make a guess:\n"))
                print(compare())
                if compare():
                    print(f"You got it, The answer is {user_number}")
                    game_over = True
                    break
                attempts_left = attempts_left - 1
                print(f"You have {attempts_left} attempts remaining to "
                      f"guess the number\n")
        if attempts_left == 0:
            game_over = True
            print("Game over. You have no attempts left!")

    def play_again():
        """Function asks user if he wants to play again"""
        start_again_reply = input("Do you want to start the game "
                                  "again? Please type 'y' or 'n'").lower()
        if start_again_reply == 'y':
            game()
        else:
            print("Thank you for playing! Goodbye!")
            quit()

    play_again()

game()
