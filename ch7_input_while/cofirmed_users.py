#moving items from one list to another

full_list = [1, 2, 3, 4]
empty_list = []

while full_list:
    print(full_list)
    txfr = full_list.pop()
    empty_list.append(txfr)
    print(empty_list)

print('\n') 

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user:" + current_user.title())
    confirmed_users.append(current_user)

print('\nthe following users have been confirmed')

for user in confirmed_users:
    print(user.title())
    
    
    
