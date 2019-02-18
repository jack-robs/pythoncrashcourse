#copy a list using slices 

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('grapefruit')
friend_foods.append('dogmeat') 


print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite foods are:')
print(friend_foods)

print('using for loops:\n')

print('My favorite foods are:')

for my_food in my_foods:
	print('\t', my_food)

print('\n')
print('My friend\'s favorite foods are:')	
for friend_food in friend_foods:
	print('\t', friend_food)
	

