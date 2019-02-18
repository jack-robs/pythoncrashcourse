#30Aug18 Jack Robertson 
#6-4: make loop for k/v of a dict that acts as a glossary for programming terms

prog_terms = {'Python': 'A programming language', 
            'Geany': 'A text editor',
            'variable': 'Used to store data',
            'integer': 'any real number',
            'floating point': 'a number with a decimal',
            '**': 'Python syntax for exponent, e.g. 2 ** 2 = 4',
            '==': 'test for equivalence.... remember "TEST"',
            '=': 'set equal to...... remember "SET"',
            'for loop': 'iterate over code, enumerated by number of elements',
            }

for term, definition in prog_terms.items():
    print(term + ': ' + definition + '\n')

#add more terms

prog_terms['computer'] = 'thing used to write code'
prog_terms['while loop'] = 'loop over set of code while determined condition is true'
prog_terms['white space'] = 'extra space in code, some languages like python interpet it, or ignore it'
prog_terms['list'] = 'a mutable group of ordered elements in []\'s'
prog_terms['tuple'] = 'an immutable group of ordered elements in ()\'s'

print('\n')
for term, definition in prog_terms.items():
    print(term + ': ' + definition + '\n')
