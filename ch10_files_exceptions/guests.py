#19.09.2018

"""
1) Prompt user for name
2) write input to file called guest.txt
3) read that file
"""


users_name = input("Please enter user name ")

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    guest_save = file_object.write(users_name)

#conirm write to file
with open(filename) as file_object:
    read = file_object.read()
    print(read)
    
#make a guest book 

filename = 'guestbook.txt'

enter_guests = True

while enter_guests:
    print('Hello, please enter your guest names! If finished, enter "done"')
    guest_name = input('guest name, First Last:')
    if guest_name == 'done':
        break
    with open(filename, 'a') as file_object:
        file_object.write(guest_name + '\n')
    
with open(filename) as f:
    file = f.readlines()
    print(file)
    
    
    
    
    
    

