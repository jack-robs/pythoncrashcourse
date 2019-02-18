#16.09.2018


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

print(get_formatted_name('jimi', 'hendrix'))
print(get_formatted_name)
musician = get_formatted_name('jim', 'morrison')
print(musician)

print('\n***Optional Arguements***')

def get_formatted_name2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name: #is true, i.e. is not an empty string
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    
    return full_name.title()

musician_1 = get_formatted_name2('stevie', 'wonder')
politician_1 = get_formatted_name2('j', 'hoover', 'edgar')

print(musician_1)
print(politician_1)
