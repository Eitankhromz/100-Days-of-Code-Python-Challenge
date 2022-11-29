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

 #OR

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Usually you name object the snake case of the class
coffee_menu = Menu()
make_drink = CoffeeMaker()
transaction = MoneyMachine()

machine_on = True

while machine_on:
    user_order = input(f"What would you like? ({coffee_menu.get_items()}): ")

    if user_order == "off":
        machine_on = False
    elif user_order == "report":
        make_drink.report()
        transaction.report()
    else:
        if coffee_menu.find_drink(user_order):
            drink = coffee_menu.find_drink(user_order)
            if make_drink.is_resource_sufficient(drink):
                if transaction.make_payment(drink.cost):
                    make_drink.make_coffee(drink)
