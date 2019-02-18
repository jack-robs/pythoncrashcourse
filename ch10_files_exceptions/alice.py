#20.09.2018

#trying to read a file that doesn't exist

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else: 
    #count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

