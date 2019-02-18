#16.09.2018
#Paring Lists + Fxns + For Loops

#create a function, with param\names
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

#create list to feed as argument @ function call    
usernames = ['hannah', 'ty', 'margot',]

#function call, w/ prior created list as argument, each list item feeds into list 1 at a time
greet_users(usernames)
