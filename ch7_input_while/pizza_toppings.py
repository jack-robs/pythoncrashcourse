#7-4 Pizza Toppings, While Loops

'''
1) Write WL that prompts user to enter a series of pizza toppigns
2) exit WL w/ 'quit' 
3) print prompt after True 'adding topping'
'''

#while loop easy, while x != 'quit':

prompt = "Please tell me the pizza toppings you'd like"
prompt += "\nOnce you've entered all the toppings you want, enter 'quit' "

#VEIWL
entered_toppings = ""

while entered_toppings != 'quit':
    entered_toppings = input(prompt)
    #easier method
    
    if entered_toppings != 'quit':
        print(entered_toppings)
    else:
        print('making pizza now') 
        
'''    
    if entered_toppings == 'quit':
        print('Ok making piza now')
    else:
        print('Adding ' + entered_toppings)
'''

#while loop flags, active = True, while active:
prompt = "Please tell me the pizza toppings you'd like"
prompt += "\nOnce you've entered all the toppings you want, enter 'quit' "
print("\n")
active = True
while active:
    
    entered_toppings = input(prompt)
    if entered_toppings == 'quit':
        print("\nMaking pizza now")
        active = False
    else:
        print(entered_toppings)
        


#while loop break
print("\n**8While loop, break")
prompt = "Please tell me the pizza toppings you'd like"
prompt += "\nOnce you've entered all the toppings you want, enter 'quit' "

#VEWIL
entered_toppings = ""

while True:
        entered_toppings = input(prompt)
        
        if entered_toppings == 'quit':
            break
        else:
            print(entered_toppings, "\n")
    
    
