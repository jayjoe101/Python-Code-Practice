total = int(input("Welcome to the tip calculator\nWhat was the total bill?: $"))
percent = 1 + float(input("What percentage tip would you like to give?: ")) / 100
people = int(input("How many people to split the bill?: "))

print (f'Each person should pay: ${total / people * percent:.2f}') # :.2f saves two decimals no matter what