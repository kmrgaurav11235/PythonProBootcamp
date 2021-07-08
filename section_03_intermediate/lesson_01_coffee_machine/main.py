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


def check_resources(drink_ingredients):
    for ingredient_name in drink_ingredients:
        quantity_required = drink_ingredients[ingredient_name]
        quantity_present = resources[ingredient_name]
        if quantity_required > quantity_present:
            return [False, ingredient_name]
    return [True]


def check_money(total_cost, num_quarters, num_dimes, num_nickles, num_pennies):
    total_payment = num_quarters * 0.25 + num_dimes * 0.1 + num_nickles * 0.05 + num_pennies * 0.01
    if total_cost > total_payment:
        return [False, 0.0]
    else:
        return [True, (total_payment - total_cost)]


def modify_resources(ingredients_used, total_cost):
    global money
    for ingredient_name in ingredients_used:
        resources[ingredient_name] = resources[ingredient_name] - ingredients_used[ingredient_name]
    money = money + total_cost


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

        resources_check_result = check_resources(ingredients)
        are_resources_sufficient = resources_check_result[0]
        if are_resources_sufficient:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            check_money_result = check_money(cost, quarters, dimes, nickles, pennies)
            is_enough_money_inserted = check_money_result[0]

            if is_enough_money_inserted:
                modify_resources(ingredients, cost)
                change = check_money_result[1]
                print(f"Here is ${round(change, 2)} in change.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {resources_check_result[1]}!")
    else:
        print("Invalid Choice!")

