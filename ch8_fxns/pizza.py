#16.09.2018
#Fxns w/ arbitary number of params


def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
    
make_pizza('pepperoni', 'cheese', 'anchovies')
make_pizza('chicken', 'pinneaple')

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
            "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
    
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'zebra meat', 'water cheese')
