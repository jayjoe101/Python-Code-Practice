from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMenu = Menu()
coffeeMachine = CoffeeMaker()
money = MoneyMachine()

while True:
    user_input = input('What would you like (espresso/latte/cappuccino): ')
    if user_input == 'q':
        break
    elif user_input == 'report':
        coffeeMachine.report()
    elif coffeeMenu.find_drink(user_input):
        coffee = coffeeMenu.find_drink(user_input)
        if coffeeMachine.is_resource_sufficient(coffee):
            if money.make_payment(coffee.cost):
                coffeeMachine.make_coffee(coffee)


