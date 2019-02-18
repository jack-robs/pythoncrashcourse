#16.09.2018

#8-3: fucntion accepts size and text that prints on a t-shirt
#call fxn w/ positional arguments
#call fxn w/ keyword arguments 

def make_shirt(shirt_size='large', shirt_text='i love python'):
    print('\nYou have requested a ' + shirt_size.title() + ' shirt.')
    print("'" + shirt_text.title() + "'" + ' will be printed on the shirt.')

make_shirt('medium', 'hello world')
make_shirt(shirt_size='large', shirt_text='positional argument')
make_shirt()
make_shirt(shirt_size='medium', shirt_text='i love c')
make_shirt('medium', 'i love ruby')


