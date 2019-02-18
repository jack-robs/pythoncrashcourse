'''
Build refactored login sequence

login_engine():
    -call up current .json, store output in variable 
    -ask new user, is read(json-variable) current user?
    -if not, get_new_user_name(store new user, write over last file)
'''
import json

def call_current_user():
    filename = 'username.json'
    try: 
        with open(filename) as f_obj: 
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username 

def get_new_username():
    filename = 'username.json'
    username_new = input("What do you want your username to be?... ")
    with open(filename, 'w') as f_obj:
        json.dump(username_new, f_obj)
    print(username_new + ', your data is stored for next time')

def login_engine():
    username = call_current_user()
    engine_active = True
        
    while engine_active: 
        verify_user = input("Is this you 'yes', 'no': " + username + ".. ")
        
        if verify_user == 'yes':
            print('Welcome back, ' + username + ', your username is already stored')
            break
        elif verify_user == 'no':
            get_new_username()
            break
        else:
            none
            
login_engine()
    
    

    
