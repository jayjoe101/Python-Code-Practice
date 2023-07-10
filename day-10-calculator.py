def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def math_dict(operation, a, b):
    math = {
        '+':add(a,b),
        '-':subtract(a,b),
        '*':multiply(a,b),
        '/':divide(a,b),
    }
    return math[operation]

while True:
    x = int(input('Whats the first number?: '))
    op = input('+\n-\n*\n/\nPick a operator: ')
    y = int(input('Whats the second number?: '))

    print(f'{x} {op} {y} = {math_dict(op, x, y)}')
    
    if input('Want to make another calculation? "y" or "n": ') == 'n':
        break