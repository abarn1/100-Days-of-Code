from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# need to build a while loop to ask the next customer what they want
machine_state = True
menu_items = Menu()
machine_resources = CoffeeMaker()

while machine_state:
    order = input(f'What would you like? {menu_items.get_items()}: ')
    if order == 'off':
        machine_state = False
    elif order == 'report':
        print(machine_resources.report())