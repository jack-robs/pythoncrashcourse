#28Aug18, Jack Robertson, 30Aug18(nesting example)
#make a simple dictionary, print out k/v

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

#add new value to dict
print('\n****Add new value to Dict')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


#add values to empty dict
print('\n***Add values to empty dict')

alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


#modify values to existing kys 
print('\n****Modify values to existing keys')

alien_0 = {'color': 'green'}
print('This alien is ' + alien_0['color'] + '.')

#change value for k: 'color'
alien_0['color'] = 'yellow'
print('This ailen is now ' + alien_0['color'] + '.')


#use dicts to track alien's position at different movement speeds
print('\n***Tracking alien movement')

alien_0 = {'x_position' : 0, 'y_position': 25, 'speed' : 'medium'}
print('Original x-position: ' + str(alien_0['x_position']))


#Move alien to the right
#Determine how far to move alien, based on current speed (by x-increment)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3

#new position: old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_position']))


#delete k-v pairs
print('\n**Delete k-v pairs')

alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#nesting
print('\n***Nesting dicts in list')
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15} 

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


#store generated dicts in a list w/ loop
print('\n****Store generated dicts in a list w/ loop')

aliens = []

#make 30 green aliens
for alien_number in range(30): #remember count from 0
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#print first 5 aliesns
for alien in aliens[:5]:
    print(alien)
print('....')

#show how many aliens have been created
print('Total number of aliens: ' + str(len(aliens)))

#change first three aliens to new characteristics
print('\n')
#for shell-variable alien in the list aliens, so var = dict (overall)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)



































