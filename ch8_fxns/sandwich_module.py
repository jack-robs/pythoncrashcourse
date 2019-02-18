def sandwiches_fxn(bread, *toppings):
    """Print sandwich and it's toppings"""
    print('\nOn your ' + bread + ' sandwich:')
    for topping in toppings:
        print("- " + topping) 
