from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_coffee_machine_on = True

while is_coffee_machine_on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "off":
        is_coffee_machine_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        ordered_drink = menu.find_drink(user_choice)
        if ordered_drink is not None and coffee_maker.is_resource_sufficient(ordered_drink) \
                and money_machine.make_payment(ordered_drink.cost):
            coffee_maker.make_coffee(ordered_drink)
