from Ceasar_Cipher_logo import *

# Start again
start_again = False
while not start_again:

    # Greet function
    def greet():
        print(logo)
        print("WELCOME TO CEASAR CIPHER GAME!")
    greet()

    # Option input by user

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift >= 26:
        shift = shift%26

    # Function encrypt that takes the text and shift as inputs

    def ceasar(start_text, shift_amount, cipher_direction):
        end_text=""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabet:
                index_of_text = alphabet.index(letter)
                new_index = index_of_text + shift_amount
                end_text += alphabet[new_index]
            else:
                end_text+=letter
        print(f"The {cipher_direction}d text is {end_text}")

    # Function encrypt that takes the text and shift as inputs

    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask user if want to start again

    start_again = input("Would you like to start again? Type yes or no:\n").lower()
    if start_again == "yes":
        start_again = False
    else:
        print("Goodbye!")