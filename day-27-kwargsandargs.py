# unlimited args in a function
# the syntax is *keyword (args can be anything) but args is default
def add(*args): # use *args to make things more robust
    return sum(args)
print(add(2, 3, 5))

# what if you wanted unlimited keyword arguments?
# use kwargs again the syntax is **name
def calculator(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        n += kwargs['add']
        n *= kwargs['multiply']
    
calculator(2, add=3, multiply=4) # you can pass key word arguements and then refrence them by name

class Car():
    # this is the major use of optional keyword arguements
    def __init__(self, **kw):
        self.make = kw.get('make') # use get becuase it will return none instead of breaking if it doesnt exist
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.year = kw.get('year')

my_car = Car(make='Honda',model='Civic')
print(my_car.year)
print(my_car.make, my_car.model)