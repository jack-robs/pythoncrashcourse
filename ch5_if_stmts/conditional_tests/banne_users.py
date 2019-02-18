#checking if strings  are not in a list

banned_users = ['andrew', 'carolina', 'david']

banned_user = 'marie'

if banned_user not in banned_users:
    print(f'Our database is secure, {banned_user.title()} isn\'t in it') 
    

user = 'steve'

if user not in banned_users:
    print(user.title() + ', you can post if you\'d like')
n
