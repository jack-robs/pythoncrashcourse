#24Aug18
#using if-elif-else:


'''
Situation:
based on age, admission to park:
under 4: free
age 4 to 18: $5
age 18 and up: $10
'''

age = 17
if age < 4:
    print('Your admission is free')
elif age < 18:
    print('Your admission is $5')
else:
    print('Your admission is $10')


#book answer

age = 12
if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10.')
    
    
#more effecient, print output in final roll up

age = 62

#these stmts will set value of price to a int, which is then stored and
#can be used once out of the conditional tests
#this is also easy to modify, more modular code
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:                   #i can omit else
    price = 5

print('Your cost of admission is $' + str(price))
