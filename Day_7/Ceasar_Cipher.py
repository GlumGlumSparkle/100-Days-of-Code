from Ceasar_Cipher_logo import *

# Greet function
def greet():
    print(logo)
    print("WELCOME TO CEASAR CIPHER GAME!")
greet()

# Option input by user
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Function encrypt that takes the text and shift as inputs

def encrypt(plain_text, shift_amount):
    chipher_text = ""
    for letter in plain_text:
        index_of_text = alphabet.index(letter)
        new_index = index_of_text + shift_amount
        chipher_text += alphabet[new_index]
    print(f"The encoded text is {chipher_text}")

# Function encrypt that takes the text and shift as inputs

def decrypt(chipher_text, shift_amount):
    plain_text = ""
    for letter in chipher_text:
        index_of_text = alphabet.index(letter)
        new_index = index_of_text - shift_amount
        plain_text += alphabet[new_index]
    print(f"The encoded text is {plain_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
if direction == "decode":
    decrypt(chipher_text=text, shift_amount=shift)


