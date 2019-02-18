#05.09.2018 input()

message = input("Tell me something, and I will repaet it back to you: ")
print(message)


#do this with a while loop
print('\n****While loop')

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

#do this, but exit program w/ input('quit'), vs. executing it, and then quit
print('\n')
print('new loop')

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)


#flag use
print('\n***Using a Flag with while loops')
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True #starts program in an active state 
while active: #is true....
    message = input(prompt)
    #checks value of input right after user enters it
    if message == 'quit':
        active = False #breaks loop
    else:
        print(message) 
        
