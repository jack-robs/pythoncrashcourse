#16.09.2018
#Functions: return a dictionary 

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age: #is true, in that a value is inputted, bc non-empty str = True
        person['age'] = age #store that in a new k-v in person{}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

musician_2 = build_person('jimi', 'hendrix', age=27)
print(musician_2)
