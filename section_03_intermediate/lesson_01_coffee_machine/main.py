MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
is_coffee_machine_on = True


def print_report():
    """Print report about the resources left in the coffee machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


user_choice = input("What would you like? (espresso/latte/cappuccino):")

if user_choice == "off":
    is_coffee_machine_on = False
elif user_choice == "report":
    print_report()

# TODO 1.3:  The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.

# TODO 4.1: Check resources sufficient?

# TODO 5.1: Process coins

# TODO 6.1: Check that the user has inserted enough money to purchase the drink they selected

# TODO 6.2: If the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time "report" is triggered.

# TODO 6.3: If the user has inserted too much money, the machine should offer change.

# TODO 7.1:  If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.

# TODO 7.2: Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
