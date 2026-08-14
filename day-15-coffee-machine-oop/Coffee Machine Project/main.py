from coffee_data import menu, profit, resources


def report():
    print(f"Water: {resources['water']}\n" 
          f"Milk: {resources['milk']}\n" 
          f"Coffee: {resources['coffee']}\n" 
          f"Money: ${profit:.2f}")

def make_coffee(drink):
    ingredient_list = ["water", "milk", "coffee"]
    for ingredient in ingredient_list:
        if ingredient in menu[drink]["ingredients"]:  # Ensure ingredient exists
            if resources[ingredient] < menu[drink]["ingredients"][ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
            resources[ingredient] -= menu[drink]["ingredients"][ingredient]
    return True

def make_transaction(drink):
    global profit
    try:
        print("Please insert coins.")
        quarters = int(input("Quarter count: "))
        dimes = int(input("Dime count: "))
        nickels = int(input("Nickel count: "))
        pennies = int(input("Penny count: "))
    except ValueError:
        "Please put a numerical value."

    total_inserted = quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01
    if total_inserted < menu[drink]["cost"]:
        print("Sorry, not enough coins. Money refunded")
        return False
    else:
        dollar_change = total_inserted - menu[drink]["cost"]
        profit += menu[drink]["cost"]
        if dollar_change != 0:
            print(f"Here is {dollar_change:.2f} dollars in change.")
        return True

def order():
    machine_on = True
    coffee_list = ["espresso", "latte", "cappuccino"]
    while machine_on:
        drink_prompt = input("\nType \"report\" for printing a formatted report\nt" +
                            "and \"off\" for turning off the coffee machine\n" +
                            "What would you like? (espresso/latte/cappuccino):").lower()
        if drink_prompt == "off":
            machine_on = False
            print("Machine shutting down, have a good day")
        if drink_prompt == "report":
            report()
        if drink_prompt in coffee_list:
            can_make_coffee = make_coffee(drink_prompt)
            if not can_make_coffee:
                return
            else:
                can_make_transaction = make_transaction(drink_prompt)
                if not can_make_transaction:
                    return
                print(f"Here is your {drink_prompt}. Enjoy!")

order()

