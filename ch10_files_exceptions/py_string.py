#19.09.2018 
#read/print a long string from a file

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()          

#merge into one big string
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

#is my birthday in pi

birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday is in the first million digits of pi! ")
else:
    print("Your birthday does not appear to be in the first million digits of pi.")
    
    
