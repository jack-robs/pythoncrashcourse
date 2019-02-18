#15.09.2018 

sandwich_orders = ['pastrami','italian combo', 'mozzarella and prosciutto', 'cuban',
                    'chicken cutlet', 'pastrami', 'pastrami']

print('The deli has run out of pastrami unfortunately')
print('Current orders are as follows ' + str(sandwich_orders))

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('New orders are as follows ' + str(sandwich_orders))


