#16.09.2018
#Modifying a list in a function


"""Modifying a list into another, not using a function"""

#designs that need to be printed, move from upd to pd lists
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printing each design, until none are left
#move each design to completed_models[] after printing

while unprinted_designs: #is true, bc a list is True if it has values in it
    current_design = unprinted_designs.pop() #pop off end item 
    
    #simulate printing a 3D model from the pop() design 
    print("While loop Printing model: " + current_design)
    completed_models.append(current_design) 

#Display all completed models
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)


"""Do this with functions: 1xFxn handles printing designs, 1xFxn summarize prints"""
print('\n"""Do this with functions: 1xFxn handles printing designs, 1xFxn summarize prints"""')


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to complete_models after printing.
    """
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #simulate printing 3d model from design
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case2', 'robot pendant', 'dodechaedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
        
        
        
        
