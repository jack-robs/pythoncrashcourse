#Method 1: import whole module
import pizza_module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(16, 'pepperoni', 'pete hair')


#Method 2: import specifc fxn from module
from pizza_module import make_pizza

make_pizza(16, 'cheese', 'salami')

#Method 3: fxn alias

from pizza_module import make_pizza as mp
mp(14, 'no sauce', 'extra cheese')

#Method 4: module alias

import pizza_module as p

p.make_pizza(11, 'cheese', 'more cheese')

#Method 5: Import all functions in module 

from pizza_module import *

make_pizza(10, 'cheese', 'zebras')

