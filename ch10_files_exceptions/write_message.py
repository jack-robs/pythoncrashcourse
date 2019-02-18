#19.09.2018

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    dog = file_object.write("I love programming")
    #prints out string length, which is odd
    print(dog)


with open(filename, 'w') as file_object:
    file_object.write("This is line one.\n")
    file_object.write("This is line two.\n")
    
with open(filename) as f:
    print(f.read())


#append to a file

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in larg datasets. \n")
    file_object.write("I love creating apps that can run in a browser. \n")
    
with open(filename) as f:
    print(f.read())
