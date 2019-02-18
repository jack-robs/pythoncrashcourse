#15.09.2018

#position arguments in functions

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')

#multiple function calls

#positional argument
describe_pet('dog', 'willie')

#keyword argument
describe_pet(animal_type='horse', pet_name='steve')
describe_pet(pet_name='steve', animal_type='horse')

#default values
print('\n**Default Values**')
def describe_pet(pet_name, animal_type='dog'):
    print('\nI have a 2pet named ' + pet_name + '.')
    print(pet_name + ' is a ' + animal_type)
    

describe_pet('willie')
describe_pet('willie', 'horse')
describe_pet(pet_name='jeremiah', animal_type='zebra')

describe_pet()





