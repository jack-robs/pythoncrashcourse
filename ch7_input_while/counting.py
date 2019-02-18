#Ch 7 while loop example 1 

current_number = 1
while current_number <= 5:
    print(current_number) 
    current_number += 1

#use continue to print out only odd numbers 
print("\n***Using $continue to print out only odd numbers")

#create initial while loop value to initiate 'entrance into while' EIWL
current_number = 0
#start loop
while current_number <10:
    current_number += 1
    if current_number % 2 == 0:
        continue #if the number is even, return to start of loop next #
    
    print(current_number)
    


