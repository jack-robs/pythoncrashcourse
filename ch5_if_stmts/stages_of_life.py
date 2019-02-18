#if-elif-else, determine stages of life

age = 10

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print('The person is a ' + str(stage) + ' at age ' + str(age))

