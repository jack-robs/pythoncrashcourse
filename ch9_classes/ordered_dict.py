from collections import OrderedDict

glossary = OrderedDict()

glossary['python'] = 'a computer language'
glossary['for loop'] = 'iterate over discrete amount of code'
glossary['while loop'] = 'iterate over code while condition is true'
glossary['list'] = 'ordered data structure, callable by order'

for term, definition in glossary.items():
    print(term.title() + ': ' + definition)

  
