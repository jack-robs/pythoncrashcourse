#store same info about multiple parties

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
    
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() +
    '.')


#use a for loop to print all k/v
print('\n**Using a For Loop')
for name, language in favorite_languages.items():
    print('\nName: ' + name)
    print('Language: ' + language)

#or
    print(name.title() + "'s favorite language is " + 
            language.title() + '.')


#for loop, only keys
print('\nPrint only Keys')

for name in favorite_languages.keys():
    print(name.title())


for name in favorite_languages:
    print(name.title())


#use if statements with for loop, and 2x dicts 
print('\n***Use if statements to pull results from two dicts together during', 
'loops')

friends = ['sarah', 'phil']

for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + 
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")
        
        
if 'erin' not in favorite_languages.keys():
    print('Erin, what\'s your favorite language?')
    
    
#use sorted() to print keys in order
print('\n**** Use sorted() to print keys in order from dict w/ for loop')

for names in sorted(favorite_languages.keys()):
    print(names.title() + ', thank you for taking the poll.')
    



#use values() to print only values in for loop 
print('\n***Use values() to print only values in for loop')

print('The following languages have been mentioned:')
for languages in favorite_languages.values():
    print(languages.title())


print('\nThese are the languages, no repeats:')
for language in set(favorite_languages.values()):
    print(language.title())

 
#Exercise 6-6: Polling 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


poll_takers = ['jen', 'andrew', 'ken', 'ali', 'edward', 'steve']

for names in poll_takers:
    
    if names in favorite_languages.keys():
        print('thanks for taking the poll ' + names + '!')
    else:
        print('Please take the poll ' + names + '!')

#Use list in a dict so users can have multiple favorite languags 
print('\***Use a list in a dict so users can have multiple favorite langs')

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }


for name, language in favorite_languages.items():
    print('\n' + name.title() + "'s favorite language is:")
    for choice in language:
        print('\t' + choice)
