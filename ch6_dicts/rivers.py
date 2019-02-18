#30Aug18 Jack Robertson 
#make dictionary of three rivers (k) and country (v)

rivers = {
        'nile': 'egypt', 
        'amazon': 'brazil', 
        'mississippi': 'america',
        }
    

for river, country in rivers.items():
    print('\nThe ' + river.title() + ' runs through ' + country.title())
    
print('\n')
for river in rivers.keys():
    print(river.title())
print('\n')
for country in rivers.values():
    print(country.title())
