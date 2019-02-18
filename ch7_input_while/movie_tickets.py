#7-5 movie tickets while loops

'''
-age -> ticket price
    age < 3: free
    age < 12: $10
    age > 12: $15
-write while loop, w/ break
'''

prompt = "Please tell me your age, and I'll tell you ticket price "
prompt += "\nOtherwise, enter 'quit' to quit program: "

#VEWL
age = ""

while True:
    age = input(prompt)
    
    if age == 'quit' or ' ':
        break
    
    age = int(age)
    
    if age < 3:
        price = 'free'
    elif age < 12:
        price = 10
    else:
        price = 15
    
    if price == 'free':
        print('Your ticket price is ' + price + "\n")
    else:
        print('Your ticket price is $' + str(price) + "\n")
