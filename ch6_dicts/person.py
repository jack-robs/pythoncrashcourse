#28Aug18 Jack Robertson 
#dict to store info about a person I know

person_know = {'first name': 'Alison', 'last name': 'Robertson', 
                'city': 'Boston'}
    
print('Person\'s name is ' + person_know['first name'])
print('Person\'s last name is ' + person_know['last name'])
print('Person lives in ' + person_know['city'])
    
print('\n****Nested dicts in list')

person_1 = {'first name': 'jack', 'last name': 'robertson', 
            'city': 'fort drum'}

person_2 = {'first name': 'dale', 'last name':'macgreggor',
            'city': 'wheeling'}

person_3 = {'first name': 'jones', 'last name':'stevenson',
            'city': 'topeka'}
            
people = [person_1, person_2, person_3]

for person in people:
   # print('First name: ', person['first name'])
    for k, v in person.items():
        print(k, ': ', v)
