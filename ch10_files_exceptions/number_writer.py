#20.09.2018
#writing/loading json

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers, f_obj)
    
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

