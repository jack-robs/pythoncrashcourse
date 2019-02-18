"""
1) while loop
2) ask peope why they like programming
3) answer: add reason to afile that stores the responses
"""


#prints instructions
print("This will be a poll on why you like programming, please follow instructions.\n")
input()
print("If you'd like to wipe the file, follow instructions when prompted")
print("If you'd like to read the current file, follow instructions when prompted")

#starts program w/ Flag
prog_run = True
#starts while loop, based on prog_run Flag
while prog_run:
    #sets filename to the file, relative path (same directory)
    filename = 'programming_poll.txt'
    #enter-to-continue
    input()

    #read file
    prompt_read = input("If you'd like to read the current file, enter 'read': ")

    if prompt_read == 'read':
        with open(filename) as read_file:
            read = read_file.read()
            print(read)
    
    #wipe file prompt: gives option
    prompt_wipe = input("If you'd like to wipe the file before beginning, enter 'wipe': ")

    #if input is correct, wipe file for fresh write
    if prompt_wipe == 'wipe':
        with open(filename, 'w') as wipe_file:
            wiped_file = wipe_file.write('')

    
    while True:
        prompt_continue = input("Continue to write to file? 'quit' or 'continue': ")
        if prompt_continue == "quit":
            break
        if prompt_continue == "continue":
            break
    
    if prompt_continue == "quit":
        break

    active = True
    while active:

        name = input('\nPlease enter your name, or "quit" to exit: ')
        if name == 'quit':
            break
        reason = input('Please enter your reason, or "quit" to exit: ')
        if reason == 'quit':
            break

        with open(filename, 'a') as file_object:
            file_object.write(name + ': ' + reason)
            file_object.write('\n')
            
        #reads file as a whole
        print("**Reading your file...***")
        with open(filename) as f:
            print_file = f.read()
            print(print_file)
    
    #exit or restart program    
    prompt_end = input("Restart program? Enter 'yes' to continue, 'no' to exit: ")
    
    if prompt_end == "no":
        break

    ''''
    #reads file line by line, w/o for loop, will output as a list, 1xline:index
    with open(filename) as f:
    print_file = f.readlines()
    for line in print_file:
    print(line)
    '''

