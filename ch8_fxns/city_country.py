#16.09.2018
#8-6 City names. fxn takes name of city/country, return formatted str
#call it 3x, print returned values


def city_country(city, country):
    city_country_pair = city.title() + ', ' + country.title()
    return city_country_pair
    
pair1 = city_country('fort worth', 'u.s.a.')
pair2 = city_country('dallas', 'u.s.a')
pair3 = city_country('boston', 'u.s.a.')

print(pair1)
print(pair2)
print(pair3)
