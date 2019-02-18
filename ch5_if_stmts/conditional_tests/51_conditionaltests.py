#write series of conditional tests
#in, not in, or, and, numerical (>, <, !=, ==,)

#1, T, in
supply_room = ['ingles', 'medina', 'robertson']
print('robertson' in supply_room, 'Predict True')

#

#2, F not in
print('I predict false:', 'kahue' in supply_room)

#3, T, or
print('I predict true:', 15 >= 15 or 13 > 17)

#4, T, and
print('I predict True:', 15 == 15 and 12 != 11)

#5->, T
base_value = 10
conditional_list_test = [1, 20, 12, 55, 1.5]
for test_value in conditional_list_test:
    print(base_value > test_value)



#equality and inequality in strings

str_test = 'audi'
print('\nString test')
print('True:', 'Audi'.lower() == 'audi')
print('False:', 'a u d i' == 'audi')


#lower() function 
lower_test = 'jambalya'
print('\n',
'True:', 'Jambalya'.lower() == lower_test,
'\n','False:', 'Dog'.lower() == lower_test)

#numerical tests, =, !=, >, <, >=, <=
numerical_test = []

for number in range(1, 50, 4):
    numerical_test.append(number)
    
print(numerical_test)

test_value = 23.5
for test in numerical_test:
    print(
    test_value == test,
    test_value != test,
    test_value > test,
    test_value < test,
    test_value >= test,
    test_value <= test
    )


#tests with and and or
test_value = 15
for test in numerical_test:
    print(test_value > test) 
 
