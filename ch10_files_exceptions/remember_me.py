import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try: 
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username 

def verify_user():
    '''Function call to see if user logging in is new'''

def greet_user():
    """Greet the user by name."""
    username = get_stored_username() #tie in previous function 
    if username:
        print("welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")

greet_user()
            
    
    
    
    
    
S
