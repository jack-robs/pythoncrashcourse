#8-7 Album
#16.09.2018

"""
1. fxn that builds dict describing a music album, artist and album title
2. return dict 
3. build 3x dicts for diff albums
4. print returns
5. go back: add option param for album in fxn, number of tracks, build 
if statement for it to store as dict. 
6. Do 3x calls to reflect his new inclusion 
"""


def make_album(artist, album_title, number_tracks=''):
    music_dict = {'artist': artist, 'album tile': album_title}
    return music_dict
    
album1 = make_album('the doors', 'the doors hotel')
album2 = make_album('jimi hendrix', 'purple haze')
album3 = make_album('led zeppelin', 'led zeppelin IV')

print(album1)
print(album2)
print(album3) 

print('\****User Albums****')

#FEWL made
#DEWL made

while True:
    print("\nYou'll be prompted to enter an artist name and album title.")
    print("(type 'q' to quit at any time)\n")
    
    artist = input("Enter artist name: ")
    if artist == 'q':
    
        break
    
    album = input("Enter album title: ")
    if album == 'q':
        break
    
    album_artist = make_album(artist, album)
    print(album_artist) 
    
print('\n***Use While Loop to Store values into dictionary***')

def store_dict():
    store_dict = {}
    while True: 
        start = input('enter to start, q to exit')
        if start == 'q':
            break
        
        key = input('input key ')
        value = input('input value ')
        store_dict[key] = value 
        
        print('\n', store_dict) 
        
store_dict()
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










