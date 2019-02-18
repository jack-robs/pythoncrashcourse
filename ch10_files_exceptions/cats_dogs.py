

file1 = 'cats.txt'
file2 = 'dogs.txt'

def read_file(filename):
    """Read contents of file and print to screen"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print(contents)
    except FileNotFoundError:
        pass
        """print(filename + ' was not found!')"""
    print('done\n')

read_file('cats.txt')
read_file('dogs.txt')
read_file('geronimo.txt')

