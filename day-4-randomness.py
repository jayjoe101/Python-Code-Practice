import random

random_int = random.randint(1, 10) # outputs a random integer between 1 and 10
print(random_int)

list_of_junk = ['1', 'a', '203']
list_of_junk.extend(['some', 'extra', 'junk']) # use .extend to add a list of items to a list

print(random.choice(list_of_junk)) # will give a random element from a list