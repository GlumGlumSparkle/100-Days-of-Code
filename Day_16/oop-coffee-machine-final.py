from menu import Menu
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
"""Methods: get_items(), find_drink(order_name)"""
money_machine = MoneyMachine()
"""Methods: report(), make_payment(cost)"""
coffe_machine = CoffeeMaker()
"""Methods: report(), is_resource_sufficient(drink), make_coffe(order)"""

is_on = True
while is_on:
    options = menu.get_items()
    user_reply = input(f"What would you like?\n{options}\n").lower()
    if user_reply == "off":
        print("Machine will turn off.")
        is_on = False
    elif user_reply == "report":
        money_machine.report()
        coffe_machine.report()
    else:
        chosen_drink = menu.find_drink(user_reply)
        print(f"You have chosen: {user_reply}, Cost is:{chosen_drink.cost}")
        drink_resources = coffe_machine.is_resource_sufficient(chosen_drink)
        if drink_resources and money_machine.make_payment(chosen_drink.cost):
            coffe_machine.make_coffee(chosen_drink)

