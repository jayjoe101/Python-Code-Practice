def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    """higher order is a function which takes a functino"""
    return func(n1 , n2)

print(calculator(78, 9, multiply)) # on the call mult does not need parentheses
