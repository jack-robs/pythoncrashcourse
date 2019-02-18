#15.09.2018 User input into while loops, store in dict

responses = {}

#set a flag to indicate the polling is active
polling_active = True

while polling_active: #... is True
    #promt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    #store the responses in a dict, dict_responses 
    responses[name] = response #response = created key, name = value
    
    #Find ot if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
    
#Polling is complete. Show the results 

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to clim " + response + ".")
