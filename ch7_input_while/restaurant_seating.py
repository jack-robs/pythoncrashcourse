#7-2 Restaurant Seeting 05.09.2018

prompt = "How many people are in your dinner group? "
num_people = input(prompt)
num_people = int(num_people)

if num_people > 8:
    print('You\'ll have to wait for a table')
else:
    print('Your table is ready!')



