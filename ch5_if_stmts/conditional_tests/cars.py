
#loop through list of cars, print bmw in all caps

cars = ['audi', 'bmw', 'subaru', 'toyota']

#loop through each item in the list
for car in cars:
    #if the car value is equal to the string 'bmw',
    if car == 'bmw':
        #print that string in uppercase
        print(car.upper())
    #in every other situation
    else:
        #print the car in title case
        print(car.title())

''' 
Loop execution:
1) checks if the current value of car is 'BMW', does if stmt, 
2) otherwise, sees value is not BMW
3) prints it in title() case
'''

print('\n')
#Conditional test 1: check for equality
car = 'bmw'
print(car == 'bmw') #evals to True


print('\n')
#Test equality is case sensitive
car = 'audi'
print(car == 'Audi') #evals to False

#if case doesn't matter, can be helpful to .lower() by default on strs i test
print(car.lower() == 'audi') #is Car, made lower == 'audi', yes it is

#.lower() doesn't change the value stored originally
print(car) 
