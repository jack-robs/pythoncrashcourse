#31.08.2018 Jack Robertson 
#loop through dict in dict

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
        
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
        
    }
        


for user_name, user_info in users.items():
    print('\nUsername is: ' + user_name)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())
    
