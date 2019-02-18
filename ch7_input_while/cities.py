#Ch7 While loops 06.09.2018
#using break

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
        
prompt = "Please tell me the pizza toppings you'd like"
prompt += "\nOnce you've entered all the toppings you want, enter 'quit' "
