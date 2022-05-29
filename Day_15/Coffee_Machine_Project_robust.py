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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    resources["profit"] = profit
    money = resources["profit"]
    return f"Water: {water}ml \nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"


def check_suff(coffee):
    """returns true if order can be made otherwise prints sorry and returns false"""
    is_enough = True
    for ingredient in MENU[coffee]["ingredients"]:
        if resources[ingredient] < MENU[coffee]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            is_enough = False
    return is_enough


def process_coins():
    """process the amount of coins inputted"""
    print("Please insert coins")
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickels = float(input("How many nickels: "))
    pennies = float(input("How many pennies: "))
    total = quarters*0.25 + dimes*.1 + nickels*0.25 + pennies*0.01
    return total


def check_trans(choice, coins):
    """checks if there is enough money for the transaction to go through"""
    is_enough = True
    if coins < float(MENU[choice]["cost"]):
        print("Sorry that's not enough money. Money refunded.")
        is_enough = False

    return is_enough


def make_coffee(coffee):
    """deducts the resources for type of coffee made"""
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(report())
    else:
        sufficient_resources = check_suff(choice)
        if sufficient_resources:
            coins = process_coins()

            trans_succ = check_trans(choice, coins)
            if trans_succ:
                profit += MENU[choice]["cost"]
                change = round(coins - profit, 2)
                print(f"Here is ${change} in change")

                print(f"Here is your {choice}. Enjoy!")
                make_coffee(choice)

