#Dream Vacation 7-10, 15.09.2018

#write program that polls users about their dream vacation 

#write a prompt, store name + result
dream_vacations = {}

poll_active = True

while poll_active:
    
    name = input('What is your name? ')
    vacation = input('What is your dream vacation location? ')
    
    dream_vacations[name] = vacation
    
    continue_poll = input('Enter yes or no to continue the poll for a new name ')
    
    if continue_poll == 'no':
        poll_active = False
    
    
print('/n --- Poll Results ---')

for name, vacation in dream_vacations.items():
    print(name + ' wants to go to ' + vacation)



#print final poll results 
