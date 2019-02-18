#15.09.2018 7-8, Deli

#make list 'sandwich orders'
#fill with names of sammies

sandwich_orders = ['italian combo', 'mozzarella and prosciutto', 'cuban',
                    'chicken cutlet']

#make empty list finished_sammies

finished_sandwiches = []



#loop through list of sammie orders, print message reflect it, move it to list
#of finished sammies

for sandwich in sandwich_orders:
    print('Next order: ' + sandwich.title())
    print('Being worked on now...')
    finished_sandwiches.append(sandwich)
    print(sandwich.title() + ' ready for pickup')
    print('\n')


#print final message indiciating sammies are done

print('\nThese are the completed sandwiches:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
