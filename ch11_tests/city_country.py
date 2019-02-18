'''
1) write function() that takes 2x params: city name, country name
2) return single string in form City, Country
'''

def city_function(city, country, population):
    city_country = city.title() + ', ' + country.title() + ' - population ' + str(population)
    return city_country 
    
    
