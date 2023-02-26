from menu import beverages
from Logo import main_logo
from menu import resources

profit = 0
print(main_logo)


def chosen_coffe(user_choices):
    """Function returns user coffec choice"""
    if user_choices == "1":
        return 'Espresso'
    if user_choices == "2":
        return 'Latte'
    if user_choices == "3":
        return 'Cappuccino'
    else:
        return 0


def machine_resources():
    """Function reruns available resources when user needs to check them"""
    print("Available resorces are:")
    print(f"Water:{resources['Water']}ml")
    print(f"Milk:{resources['Milk']}ml")
    print(f"Milk:{resources['Coffee']}g")
    print(f"Money:$ {profit}")


def turn_off():
    """Function turns off the coffe machine"""
    print("Turning off")
    quit()


def if_resources_sufficient(order_ingredients):
    """Return True when order could be made and False if not"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Function returns total ammount of coins inserted by user"""
    total = int(input("How many quaters?"))*0.25
    total += int(input("How many dimes?"))*0.10
    total += int(input("How many nickles?"))*0.05
    total += int(input("How many pennies?"))*0.01
    return total


def transaction_succesfull(payment, cost):
    """Function returns True if transaction is successfull
    and False if transaction is not successfull"""
    if payment >= cost:
        change = round(payment-cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(choice, order_ingredients):
    """Function makes coffe and decuts resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink {choice}. Enjoy!")


is_on = True
while is_on:
    user_input = input("Please choose operation: 1 - Order,"
                       "2- Check resorces, 3- Turn off\n")
    print(f"You have chosen operation:{user_input}")
    if user_input == "1":
        for beverage in beverages.keys():
            print(beverage)
        user_choice = input(
            "What would you like to drink? 1- Espresso, 2- Latte,"
            " 3- Cappuccino\n")
        choice = chosen_coffe(user_choice)
        print(f"You have chosen:{choice}, "
              f"drink price {beverages[choice]['cost']}$")
        new_drink = beverages[choice]
        cost = new_drink["cost"]
        if if_resources_sufficient(new_drink["ingredients"]):
            payment = process_coins()
            if transaction_succesfull(payment, cost):
                make_coffe(choice, new_drink["ingredients"])

    if user_input == "2":
        machine_resources()
    if user_input == "3":
        is_on = False
        turn_off()


