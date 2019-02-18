#output first three items of a list

players = ['charles', 'martin', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:3])

print(players[:4])

print(players[1:])


#print last three players of slice, would continue to work as list changed in size
#print last three players of slice, would continue to work as list changed in size

print(players[-3:])

print('These are my first three players')
for player in players[:3]:
	print(player.title())
	
	

print('\n')
print('the first three items in the list:\n', players[:3])
print('\n')
print('three items from the middle of the middle of the list are:\n', players[-3:-1])
print('\n')
print('the last thre items in the list are:\n', players[-3:])

