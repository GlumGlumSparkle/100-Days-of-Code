import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice_list = [rock, paper, scissors]
choice = int(input("What do you choose? Rock-1, Paper-2 or Scissors-3?"))-1
if choice < 3 and choice>=0:
    print("Your choice:", choice_list [choice])
    index = len(choice_list)-1
    computer_choice = random.randint(0,index)
    print ("Computer's choice:", choice_list[computer_choice])
    if choice == computer_choice:
        print("It is a draw")
    elif choice == 0 and computer_choice == 2:
        print("You win!")
    elif choice == 0 and computer_choice == 1:
        print("You lose!")
    elif choice == 1 and computer_choice == 0:
        print("You win!")
    elif choice == 1 and computer_choice == 2:
        print("You lose!")
    elif choice == 2 and computer_choice == 1:
        print("You win!")
    elif choice == 2 and computer_choice == 0:
        print("You lose!")
else:
    print("You typed invalid number!")


