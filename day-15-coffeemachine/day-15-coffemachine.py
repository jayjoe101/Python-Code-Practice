from coffee_resources import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    """prints the coffe machine's available resources"""
    r = ''
    for resource in resources:
        r += f'{resource}: {resources[resource]}ml\n'
    return r.strip()

def check_money(coffee, money):
    """checks if sufficient money was allocated"""
    cost = MENU[coffee]['cost']
    if money > cost:
        return True
    return False

def calculate_cost(coffee, money):
    """returns either change or say how much was refunded"""
    cost = MENU[coffee]['cost']
    if check_money(coffee, money):
        if money > cost:
            return f"Here is ${money - cost:.2f} in change"
        return f'Thanks for your purchase.'
    else:
        return f'Thats not enough money: ${money:.2f} refunded.'

def check_resources(coffee):
    """makes sure that the coffe machine has sufficient resources to brew"""
    missing_resource = ''
    for i in MENU[coffee]['ingredients']:
         if MENU[coffee]['ingredients'][i] > resources[i]:
             missing_resource += f'{i}\n'
    return missing_resource.strip()   

def brew(coffee, money):
    """will make a coffe or print why it cant"""
    s = check_resources(coffee)
    if s:
        return f'Sorry you do not have sufficient:\n{s}'
    else:
        if check_money(coffee, money):
            for i in MENU[coffee]['ingredients']:
                resources[i] -= MENU[coffee]['ingredients'][i]
            return f'Here is your {coffee} enjoy'
        else:
            return 'Insufficient funds'


while True:
    user_input = input('What would you like (espresso/latte/cappuccino): ')
    if user_input == 'q':
        break
    elif user_input == 'report':
        print(report())
    elif MENU[user_input]:
        money = 0
        money += (float(input('How many quarters?: ')) * .25)
        money += (float(input('How many dimes?: ')) * .10)
        money += (float(input('How many nickles?: ')) * .05)
        money += (float(input('How many pennies?: ')) * .01)
        if calculate_cost(user_input, money) != f'Thats not enough money: ${money} refunded.':
            print(calculate_cost(user_input, money))
            print(brew(user_input, money))
        else:
            print(calculate_cost(user_input, money))
    else:
        print('Do not understand request')