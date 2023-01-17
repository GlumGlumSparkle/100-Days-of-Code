############DEBUGGING#####################

# Describe Problem
# def my_function():
#   """In range function second number is excluded from range, must be (0, 21)"""
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# """Bug reproduced when picking up 6 only - index out of range"""
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1, 5)
# print(dice_imgs[dice_num])

# Play Computer
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# age = int (input("How old are you?"))
# if age >= 18:
#     print(f"You can drive at age {age}.")
# else:
#     print(f"You can not drive at {age}")

#Print is Your Friend
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"Total words: {total_words}")

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])