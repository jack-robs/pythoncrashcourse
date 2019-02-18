#16.09.2018
#8-9 Magicians 
#make fxn that prints name of each magician



"""Work Code"""

magicians = ['steve', 'peter', 'john', 'franklin', 'maria']
great_magicians = []

def show_magicians(magic_list):
    for name in magic_list:
        print(name.title() + ' is a magician')
    print(magic_list)
    print('\nend of 1st fxn')

#change each item in list to 'the Great [name]' 
def make_great(magic_list):
    
    print('\npre perman change' + str(magic_list))
    
    for i in range(len(magic_list)):
        name_mod = 'the Great ' + magic_list[i]
        magic_list[i] = name_mod
    
    print('\nperma change' + str(magic_list) + '\n')
    

#make new list of 'the Great [name]' based on copy param list[:]    

def make_great_return(magic_list):
    print('using return\n')
    
    for i in range(len(magic_list)):
        name_mod = 'the Great ' + magic_list[i]
        magic_list[i] = name_mod
    return magic_list

    
"""Execution Code"""

show_magicians(magicians)
make_great(magicians)


new_magic = ['steve', 'peter', 'john', 'franklin', 'maria']

new_list = make_great_return(new_magic[:])
print(new_magic)
print(new_list)

#do the same above, but with copy of list of magic names [:], return new list, store
