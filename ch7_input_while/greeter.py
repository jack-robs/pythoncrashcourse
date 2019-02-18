#05.09.2018 Ch7, input()


#basic input prompt
name = input("Please enter your name: ")
print("Hello, " + name + "!")

#multi-line prompt
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print('\nHello, ' + name + '!')


print('\n')
#int() to accept numerical input

age = input("How old are you? ")
print(age)

#spits out error, can't str() > int(), $ print(age >= 18)
#this works

age = input("How old are you? ")
age = int(age) 
print(26 >= age)

