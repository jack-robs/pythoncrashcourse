pizzas = ['prosciutto', 'plain', 'jalapeno', 'pepperoni']

for pizza in pizzas:
	print('I like ' + pizza)
	
print('I really like pizza')

pizzas.append('sicilian')

friends_pizzas = pizzas[:]

friends_pizzas.append('friend test')

print('My favorite pizza is:')
for type_pizza in pizzas:
	print(type_pizza)

print('\n')
	
print('My friend\'s favorite pizza is:')
for type_pizza in friends_pizzas:
	print(type_pizza)
	

