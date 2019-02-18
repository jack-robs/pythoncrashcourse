#alien shotdown in a game, create variable and assign it to a value


#fail test
alien_color = 'yellow'

if alien_color == 'green':
    print('You have just earned five points')

#pass test

alien_color = 'green'

if alien_color == 'green':
    print('You have just earned five points')

#alien colors two
print('Alien Colors #2')

alien_color = 'red' 

if alien_color == 'red':
    points = 5

else:
    points = 10
    
print(f'You\'ve won {points} points')

alien_color = 'green'

if alien_color == 'red':
    points = 5

else:
    points = 10

print('You\'ve won', points, 'points')
#you've won 5 points

print("You've won " + str(points) + " points")
#you've won 10 points..... w/ + add in gaps, ',' does smart gaps


#Aliens #3: if-else into if-elif-else
print('\n')

alien_color = 'green'

if alien_color == 'green':
    points = 5
    
elif alien_color == 'yellow':
    points = 10

else:
    points = 15

print(f"You've received {points} points")



#f-strings work with vars, whether vars are = strs or ints
alien_color = 'yellow'

if alien_color == 'green':
    points = '5'
elif alien_color == 'yellow':
    points = '10'
else:
    points = '15'
print(f"You've received {points} points")


alien_color = 'red'

if alien_color == 'green':
    points = 5 
elif alien_color == 'yellow':
    points = 10
else:
    points = 15
print('You\'ve received ' + str(points) + ' points')
