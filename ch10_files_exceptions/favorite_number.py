#22.09.2018

import json
'''
NO REFACTORING
def get_number():
    """Get favorite number of user"""
    filename = 'favnum_norefac.json'
    try:
        with open(filename) as f_obj:
            favnum = json.load(f_obj)
    except FileNotFoundError:
        favnum = input('What is your favorite number: ')
        with open(filename, 'w') as f_obj:
            json.dump(favnum, f_obj)
            print("We'll remember your favorite number, " + favnum + 
                    " for next time!")
    else: 
        print("Your favorite number is " + favnum)
        
get_number()
        
'''
'''
#refactoring, stage 1
def get_stored_favnum():
    """Get stored favorite number if available"""
    filename = 'favnum_refac1.json'
    try:
        with open(filename) as f_obj:
            favnum = json.load(f_obj)
    except FileNotFoundError:
        return None
    else: 
        return favnum
        
def output_favnum():
    """Output favorite numbe to user, stored or new input"""
    favnum = get_stored_favnum()
    if favnum:
        print("Your favorite number is: " + favnum)
    else: 
        favnum = input("What is your favorite number? ")
        filename = 'favnum_refac1.json'
        with open(filename, 'w') as f_obj:
            json.dump(favnum, f_obj)
            print("We'll remember your favorite number, " + favnum + " next time")
            
output_favnum()
'''

#refactoring, stage 2, more complete

def get_stored_favnum():
    """Get stored favorite number, if available"""
    filename = 'favnum_refac_comp.json'
    try: #see if the file exists
        with open(filename) as f_obj:
            favnum = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favnum

def get_new_favnum():
    """Get favorite number from user input, if not stored, write to .json"""
    favnum = input("What is your favorite number? ")
    filename = 'favnum_refac_comp.json'
    with open(filename, 'w') as f_obj:
        json.dump(favnum, f_obj)
    return favnum 

def get_favnum():
    """Get user favorite number, via pulled from file, or user input"""
    favnum = get_stored_favnum()
    if favnum:
        print("Youre favorite number is: " + favnum)
    else:
        favnum = get_new_favnum()
        print("We'll remember your favorite number for next time: " + favnum)
        
get_favnum()
    
    


    
    
    
             
        
    
    


