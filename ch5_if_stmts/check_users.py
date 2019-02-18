#Exercise 5-10: check everyone has a unique user name


current_users = ['dominate_pantera', 'PixieDust', 'doorman', 'i_love_cats', 
                'TexasAlex']

new_users = ['dominate_pantera', 'Pixiedust', 'animals_are_great', 'gaiaim',
                'bobmarley69']

for usr in new_users:
    current_user_check = [usr_current.lower() for usr_current in current_users]
    if usr.lower() in current_user_check:
        print('Username ' + usr + ' is not available')
    else:
        print('Username ' + usr + ' is available') 


