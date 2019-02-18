#30.08.2018 Jack Robertson , storing list in dicts

#make dict, w/ one k:v being k:list
pizza = {
        'crust': 'thin',
        'toppings': ['mushrooms', 'pepperoni', 'extra cheese'],
        }


#print out first key
print('You ordered a pizza with ' + pizza['crust'] + ' crust and the following',
        'toppings:')
        
#print out second key w/ list, use for loop to iterate through list contents
for topping in pizza['toppings']:
    print('\t' + topping.title())

