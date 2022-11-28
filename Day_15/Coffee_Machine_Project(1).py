from menu import MENU, resources

# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def report():
    """Prints a report of all current resources"""
    resource_list = []
    for resource in resources:
        resource_list.append(resource)

    for index in range(len(resource_list)):
        if index == 3:
            print(f"{resource_list[index]}: ${resources[resource_list[index]]:.2f}")
        else:
            print(f"{resource_list[index]}: {resources[resource_list[index]]}")



# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


def sufficient_resources(coffee_choice):
    """Checks if there are enough resources to make coffee and returns True if there is not"""
    for ingredient in MENU[coffee_choice]["ingredients"]:
        if resources[ingredient] < MENU[coffee_choice]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return True
        else:
            return False


# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

def process_coins(coffee_choice):
    """processes all the coins and returns True if not enough. Otherwise prints change"""
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))

    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

    # 6. Check transaction successful?
    # a. Check that the user has inserted enough money to purchase the drink they selected.
    # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    # program should say “ Sorry that's not enough money. Money refunded. ”.
    # b. But if the user has inserted enough money, then the cost of the drink gets added to the
    # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    # c. If the user has inserted too much money, the machine should offer change.
    # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
    # places.

    if total < MENU[coffee_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return True
    else:
        resources["money"] += MENU[coffee_choice]['cost']
        change = round(total - MENU[coffee_choice]['cost'], 2)
        print(f"Here is your change: ${change:.2f}")


def make_coffee(coffee_choice):
    for ingredient in MENU[coffee_choice]["ingredients"]:
        resources[ingredient] -= MENU[coffee_choice]["ingredients"][ingredient]
        return f"Here is your {coffee_choice}. Enjoy!"


resources["money"] = 0

# b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.
coffee_machine_on = True

while coffee_machine_on:
    ##Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_coffee_choice == "report":
        report()
    # Turn off the Coffee Machine by entering “ off ” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine. Your code should end execution when this happens.
    elif user_coffee_choice == "off":
        coffee_machine_on = False
    # elif not sufficient_resources(user_coffee_choice):
    else:
        if not sufficient_resources(user_coffee_choice):
            print("Please insert coins.")
            if not process_coins(user_coffee_choice):

                # a. Check the user’s input to decide what to do next.
                # 7. Make Coffee.
                # a. If the transaction is successful and there are enough resources to make the drink the
                # user selected, then the ingredients to make the drink should be deducted from the
                # coffee machine resources.

                print(make_coffee(user_coffee_choice))


