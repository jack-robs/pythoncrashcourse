'''
line = 'Row row row your boat'
count_words = line.count('row')
print(count_words)
'''

filename = 'chapter_10/alice.txt'

with open(filename, encoding='utf-8') as file_obj:
    count_words = file_obj.read()

def search_word_case_sens(word):
    alice_count = count_words.count(word)
    print('\n' + word + ' appears this many times:')
    print(alice_count)

def search_word_all(word):
    alice_count = count_words.lower().count(word)
    print('\nAll instances, regardless of case, of ' + word + ': ')
    print(alice_count)

search_word_case_sens('alice')
search_word_case_sens('Alice')
search_word_case_sens('ALICE')
search_word_case_sens('rabbit')
search_word_case_sens('cat')

search_word_all('alice')

