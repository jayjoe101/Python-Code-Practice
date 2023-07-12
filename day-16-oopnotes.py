# objects have have two things
# things they have (attributes/variable) a 
# and things they do (methods/functions) a method is a function of an object
# these are written in classes (the blueprint of objects)

import turtle
import prettytable # to see code right click and select goto defenition

tom = turtle.Turtle() # module.class, a module is literally another file
tom.shape('turtle')
tom.color('cyan')
tom.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# install new packages from pypi using pip in the terminal
X = prettytable.PrettyTable()
print(X)