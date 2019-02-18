#use != conditional test

requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies")


requested_toppings = ['mushrooms', 'onions', 'pinneaple']

print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)

#use multiple if statements for series of checks for True conditions
requested_topping = ['mushrooms', 'extra cheese']

if 'mushromms' in requested_toppings:
    print('Add mushrooms')

if 'pepperoni' in requested_toppings:
    print('Add pepperoni')

if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print('\nFinished making your pizza') 


print('\nUsing Conditional Statements and lists')
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#basic format 
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + '.')

print('\nFinished making your pizza') 


#incorporate conditional tests and if statemenets
print('\n**Incorporate Conditional Tests and If Statements**')

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + '.')
      
#Check if list is empty
print('\n**Check is list is empty and then run $for loop')
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('Finished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')



#Using multiple lists with if statements
print('\n**Using Multiple Lists')

#this could be a tuple, make it immutable 
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                        'pinneaple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print('Sorry we don\'t have that topping')

