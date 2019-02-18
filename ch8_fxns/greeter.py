#15.09.2018 

def greet_user():
    """Display a simple greeting."""
    print("Hello!")
    
greet_user()


def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')

greet_user('sarah')

#16.09.2018
#Using functions + While loop

print('\n***Using functions + While Loop')

#function to enter while loop FEWL
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formtated."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
#making an infinite loop, feed into function, same as VEWL reqs

while True:
    print('\nPlease tell me your name')
    print("Enter 'q' at any time to quit\n")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
        
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
