#16.09.2018
#8-12 Sandwiches

"""
1) function, param = list of sandwich toppigns
2) one param at least == *param
3) print summary of sandwich (in fxn)
4) call fxn 3x
"""

def sandwiches_fxn(bread, *toppings):
    print('\nOn your ' + bread + ' sandwich:')
    for topping in toppings:
        print("- " + topping) 
    
sandwiches_fxn('whole wheat', 'provolone', 'avocado')
sandwiches_fxn('italian bread', 'salami', 'mushrooms')
sandwiches_fxn('whole grain', 'turkey', 'tuna salad', 'lettuce')


