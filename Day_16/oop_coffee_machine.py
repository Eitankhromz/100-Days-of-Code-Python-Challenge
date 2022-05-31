from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects 
# i.e. [object] = [class]
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

# create var with boolean and loop thru the program
machine_on = True
while machine_on:
    choice = input(f"What would you like? ({my_menu.get_items()}): ")  # [object].[method()]
    if choice == "off":
        machine_on = False
    elif choice == "report":
        my_coffee_maker.report()  # [object].[method()]
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)
