""" This is the calculator program"""
from Calculator_logo import *


# Add
def add(n1, n2):
    return n1+n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    """recursion - function which calls itself, has no input and no return"""
    print(logo)

    num1 = float(input("Please input first number?\n"))
    for operation in operations:
        print(operation)
    start_again = True

    while start_again:
        operation_symbol = input("Please choose operation from above list:\n")
        num2 = float(input("What is next number?\n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1}{operation_symbol}{num2} = {answer}")

        user_reply = input(f"Would you like to choose another operation and"
                           f" continue with {answer}- type yes, if not - no\n")

        if user_reply == 'yes':
            num1 = answer
        else:
            start_again = False
            calculator()

calculator()
