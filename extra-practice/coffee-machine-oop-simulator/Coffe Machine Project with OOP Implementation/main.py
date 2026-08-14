from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)
