#Don't even ask about space & time complexity on this one lol
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
    "money": 0
}

def report():
    """returns a report of all the resources"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}"

# #TODO: Check if sufficient resources:
def check_sufficient_resources(coffee):
    """Checks if there is sufficient amount of resources for the coffee types"""
    sufficient = False
    if float(resources["water"]) < float(MENU[coffee]["ingredients"]["water"]):
        print("Sorry there is not enough water")
    elif float(resources["coffee"]) < float(MENU[coffee]["ingredients"]["coffee"]):
        print("Sorry there is not enough coffee")
    else:
        sufficient = True

    if coffee == "latte" or coffee == "cappuccino":
        if float(resources["milk"]) < float(MENU[coffee]["ingredients"]["milk"]):
            print("Sorry there is not enough milk")
        else:
            sufficient = True

    return sufficient

# TODO 3: Prompt user to insert coins by asking "how many quarters", etc
def coin_processor():
    """calculates the monetary values of coins and returns a total"""
    print("Please insert coins")
    quarters = input("how many quarters? ")
    dimes = input("how many dimes? ")
    nickels = input("how many nickels? ")
    pennies = input("how many pennies? ")
    total = float(quarters) * 0.25 + float(dimes) * 0.1 + float(nickels) * 0.05 + float(pennies) * 0.01
    return total

# TODO 4: Check user coins if they have enough
def is_enough_money(sum, coffee):
    """checks if there is enough money for the type of coffee and returns the change, otherwise returns false"""
    if sum < float(MENU[coffee]["cost"]):
        return False
    elif sum > float(MENU[coffee]["cost"]):
        change = sum - float(MENU[coffee]["cost"])
        return change

def make_coffee(coffee):
    """deducts resources when coffee made"""
    resources["water"] -= float(MENU[coffee]["ingredients"]["water"])
    resources["coffee"] -= float(MENU[coffee]["ingredients"]["coffee"])
    if coffee == "latte" or coffee == "cappuccino":
        resources["milk"] -= float(MENU[coffee]["ingredients"]["water"])


# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
def coffee_machine():
    machine_on = True
    while machine_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        machine_on =False
        if user_choice == "report":
            print(report())
            machine_on = True
        elif user_choice == "off":
            machine_on = False
            print("off") #turn off machine
        else:
            # check_sufficient_resources(user_choice)
            # Check the user’s input to decide what to do next.
            # TODO 2: Turn OFF Coffee Machine
            if check_sufficient_resources(user_choice) == False:
                machine_on = True
            elif check_sufficient_resources(user_choice) == True:
                total_amount = coin_processor()
                # TODO 5: Check if transaction was successful
                if is_enough_money(total_amount, user_choice) == False:
                    print("Sorry that's not enough money. Money refunded.")
                    machine_on = True
                else:
                    change = round(is_enough_money(total_amount, user_choice), 2)
                    resources["money"] += float(MENU[user_choice]["cost"])
                    make_coffee(user_choice)
                    print(f"You gave${total_amount}. Here is your change: ${change}")
                    # TODO 6: Dispense Coffee
                    if user_choice == "espresso":
                        print("Here is your espresso. Enjoy!")  # Make Coffee
                    elif user_choice == "cappuccino":
                        print("Here is your cappuccino. Enjoy!")  # Make
                    elif user_choice == "latte":
                        print("Here is your latte. Enjoy!")

                    machine_on = True

        ## The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

coffee_machine()

