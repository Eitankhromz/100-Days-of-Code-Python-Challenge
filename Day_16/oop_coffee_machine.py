from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_CoffeeMaker = CoffeeMaker()
my_menu = Menu()

machine_on = True
while machine_on:
    choice = input(f"What would you like? {my_menu.get_items()}: ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        my_CoffeeMaker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_CoffeeMaker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_CoffeeMaker.make_coffee(drink)
