#19.09.2018
filename = 'learned_python.txt'

with open('learned_python.txt') as file_object:
    lines = file_object.readlines()


#see what raw list looks like
print(lines)

for line in lines:
    print(line.strip())

#print it out 3x times
print_count = 3
while print_count > 0:
    for line in lines:
        print(line.rstrip())
    print('\n')
    print_count -= 1


#print contents once, entire file read
print('\n***Print file once')
with open('learned_python.txt') as file_object:S
    read = file_object.read()
    print(read)
    
#change Python to C
print('\n** *Using replace')
with open('learned_python.txt') as file_object:
    lines = file_object.readlines()


for line in lines:
    #get rid of newline, replace Python w/ C
    line = line.strip()
    #must print, .replace isn't a permanent chang
    print(line.replace('Python', 'C'))
    
    
    
