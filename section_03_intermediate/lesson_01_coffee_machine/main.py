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

# TODO 1.1: Prompt user by asking “What would you like?

# TODO 1.2: Check the user’s input to decide what to do next

# TODO 1.3:  The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.

# TODO 2.1: Turn off the Coffee Machine by entering "off" to the prompt.

# TODO 3.1: Print report.

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
