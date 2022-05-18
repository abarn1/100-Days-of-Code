from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# need to build a while loop to continuously ask the next customer what they want
machine_state = True
menu_items = Menu()
machine_resources = CoffeeMaker()
money_collector = MoneyMachine()

while machine_state:
    order = input(f'What would you like? {menu_items.get_items()}: ')


    if order == 'off':
        machine_state = False
        break
    elif order == 'report':
        print(machine_resources.report())

    order_item = menu_items.find_drink(order)

    if machine_resources.is_resource_sufficient(order_item):
        print(f'That will cost {order_item.cost}')
        money_paid = money_collector.make_payment(order_item.cost)
        if money_paid:
            machine_resources.make_coffee(order_item)
