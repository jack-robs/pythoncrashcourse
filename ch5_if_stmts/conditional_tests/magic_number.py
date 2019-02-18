#check to see if two numbers are/are not equal

answer = 17

#the conditional test 'passes', as 17 != 42, so executes indented code block
if answer != 42: 
    print("That is not the correct answer. Please try again!")


age = 19
print(
age < 21, #True
age <= 21, #True
age > 21, #False
age >= 21 #False 
)


#use $and to check simo-equality
age_0 = 22
age_1 = 18
print(
age_0 >= 21 and age_1 >=21 #false
)

age_1 = 22 

print(age_0 >= 21 and age_1 >= 21) #True


#use $or to check multiple conditions, either/both 

print('\nUsing $or to test')
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21 )
