#20.09.2018
def count_words(filename):
    """Count the approximate number of words in a file."""
    try: 
        with open(filename, encoding="utf-8") as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
    
        msg = "Sorry, the file " + filename + " does not exist"
        print(msg)
        
        '''
        $pass also works here 
        '''
    else:
        #Count the approximate number of words in the file
        words = contents.split()
        num_word = len(words)
        print("The file " + filename + " has about " + str(num_word) + " words.")

filename = "alice.txt"
count_words(filename)

filenames = ['chapter_10/alice.txt', 'chapter_10/siddartha.txt', 
            'chapter_10/moby_dick.txt', 'chapter_10/little_women.txt']
            
for filename in filenames:
    count_words(filename)
