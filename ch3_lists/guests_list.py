
#make a guest list, print message inviting them to dinner


guests = ['Ali', 'Abraham Lincoln', 'Old man blue shirt']

print('Hello ' + guests[0] + ' please join me for dinner.')
print('Hi ' + guests[1] + ' please come to my house.')
print('Hello there ' + guests[2] + ' once you\'re done.')


#change guest list

print(guests[1] + ' can\'t make it')

#delete/replace guest

guests[1] = 'Joe Johnson'

print('Hello ' + guests[0] + ' please join me for dinner')
print('Hello ' + guests[1] + ' please joine me for dinner')
print('Hello ' + guests[2] + ' please join me for dinner')

#invite three more guests

#insert new guest at beginning

guests.insert(0, 'Jeffrey Frankman')

guests.insert(3, 'Table Person')

guests.append('Jeremy Price')

print(guests)

print('Hello ' + guests[0] + ' please come to dinner.')
print('Hello ' + guests[1] + ' please come to dinner.')
print('Hello', guests[2], 'please come to dinner.')
print('Hello', guests[3], 'please come to dinner.')
print('Hello ' + guests[4] + ' please come to dinner.')
print('Hello ' + guests[5] + ' please come to dinner.')
	
#shrink guest list


print('\n now we can only invite two people to dinner')

no_1 = guests.pop(0)
print(guests)

no_2 = guests.pop()
no_3 = guests.pop()
no_4 = guests.pop()
print(guests)

print('I am sorry ' + no_1 + no_2 + no_3 + no_4 + ' we don\'t have space')


del guests[0]
del guests[0]

print(guests)


guests = ['Ali', 'Abraham Lincoln', 'Old man blue shirt']

print(guests)
print(len(guests))
