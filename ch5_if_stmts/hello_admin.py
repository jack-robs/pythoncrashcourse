#exercise 5-8, list of five user names, greet users once they log in


usr_names = ['bobbob188', 'admin', '19876greatone', 'stonec', 'doggoman']
#usr_names = []

if usr_names:
    for account in usr_names:
        if account == 'admin':
            print('Hello admin, would you like a status report')
        else:
            print('Hello ' + account + ', thank you for logging in') 
else:
    print('We need to find some users!')
