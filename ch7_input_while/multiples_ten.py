#7-3 Multiples of Ten 05.09.2018

prompt = "Please input a number, I'll tell you if it's a multiple of 10: "

multiple = int(input(prompt))

if multiple % 10 == 0:
    print(str(multiple) + " is a multiple of 10")
else: 
    print("Not a multiple of 10")
    
