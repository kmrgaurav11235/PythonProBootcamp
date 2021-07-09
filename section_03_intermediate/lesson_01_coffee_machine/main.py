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
money = 0.0
is_coffee_machine_on = True


def print_report():
    """Print report about the resources left in the coffee machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def are_resources_sufficient(drink_ingredients):
    """Returns True when order can be processed, False if ingredients are insufficient"""
    for ingredient_name in drink_ingredients:
        quantity_required = drink_ingredients[ingredient_name]
        quantity_present = resources[ingredient_name]
        if quantity_required > quantity_present:
            print(f"Sorry there is not enough {ingredient_name}!")
            return False
    return True


def process_coins():
    """Returns the total calculated from the coins inserted by the user"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_payment = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total_payment


def is_transaction_successful(money_received, total_bill):
    """Returns True if payment is accepted and False if the money is insufficient"""
    if money_received >= total_bill:
        global money
        money = money + total_bill

        change = money_received - total_bill
        print(f"Here is ${round(change, 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredients from the resources"""
    for ingredient_name in drink_ingredients:
        resources[ingredient_name] -= drink_ingredients[ingredient_name]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while is_coffee_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        is_coffee_machine_on = False
    elif user_choice == "report":
        print_report()
    elif user_choice in MENU:
        drink_details = MENU[user_choice]
        ingredients = drink_details["ingredients"]
        cost = drink_details["cost"]

        if are_resources_sufficient(ingredients):
            payment = process_coins()

            if is_transaction_successful(payment, cost):
                make_coffee(user_choice, ingredients)
    else:
        print("Invalid Choice!")
