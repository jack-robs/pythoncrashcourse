#19.09.2018 
#reading file contents

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    
    
#relative file path
with open('txt_files/pi_digits2.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    
#absolute file path
file_path = '/home/johnr00/Desktop/absolute_path.txt' 
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


#read line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
        
#read .py file- this works
'''
with open('file_reader.py') as file_object:
    contents = file_object.read()
    print(contents)
'''

#read lines, store in list
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


print(lines)
for line in lines:
    print(line.rstrip())

#read lines, combine into single string
filename = 'pi_digits.txt'

#open file. store each line of digits in a list
with open(filename) as file_object:
    lines = file_object.readlines()

#create a variable 
pi_string = ''
#add each line of the list to the string pi_string, removes \n
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string










