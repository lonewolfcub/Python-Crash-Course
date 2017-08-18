# To import anther .py file as a module, use the syntax:
import pizza_4

pizza_4.make_pizza(16, 'pepperoni')
pizza_4.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# to import a specific function from a module, use the syntax:
from pizza_4 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# after importing, the function is available to call without any additional
# syntax


# to assign an alias to a function, use the syntax:
from pizza_4 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# after importing, the function is available to call without any using the
# specified alias

# to assign an alias to a module, use the syntax

import pizza_4 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# after importing, any function in the module can be called by using the
# alias and then the module name


# to import all functions in a module, use the syntax
from pizza_4 import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# warning, this can cause clashes on larger files if you have identical
# function names in your program