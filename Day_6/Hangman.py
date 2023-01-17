import random
from replit import clear
from Hangman_art import logo, stages
from Hangman_words import word_list

# ASCII logo print
print ("\nLET'S PLAY HANGMAN!")
print(logo)

# Word shuffle from list, setting lives to 6
game_end = False
chosen_word = random.choice(word_list)
lives = 6

# Generating word length to be visible to player

display = []
for x in range(0,len(chosen_word)):
    display.append("_")
string = ""
print(string.join(display))
# Guess input

while not game_end:
    guess = input("GUESS A LETTER:").lower()
    print("YOUR GUESS IS:", guess)
    clear()

# Checking if letter was already used

    if guess in display:
        print(f"THE LETTER {guess} WAS ALREADY USED")

# Checking if guess is present in chosen word

    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

# Dedaction of lives

    if lives > 0:
        if guess not in chosen_word:
            print(f"THE LETTER {guess} IS NOT IN THE WORD!")
            lives = lives - 1
            print(stages[lives])

# If no more lives left - game over

    if lives == 0:
        print("YOU LOST!")
        game_end = True

    string = ""
    print(string.join(display))

# If word guess correctly - player won

    if "_" not in display:
        game_end = True
        print("YOU WON!")


"""
            reply = input("DO YOU WANT OT PLAY AGAIN?").lower()
            if reply == "yes":
                reply = True
            else:
                print("GAME OVER")

"""
