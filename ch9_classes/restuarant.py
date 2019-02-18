#16.09.2018
"""
1) Make a class called Restaurant()
2) class has 2x attributes: name and type
3) make method to print these attys
4) make method for restaurant hours
5) instance the restaurant
6) print each attribute, call both methods, all individually
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, hours):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.hours = hours
        
    def describe_restaurant(self):    
        print('This is a ' + self.cuisine_type + ' restaurant called ' 
                + self.restaurant_name.title())
    
    def hours_open(self):
        print(self.restaurant_name.title() + ' is open ' + self.hours)
    

china_king = Restaurant('china king', 'chinese food', '0500-2100')

print(china_king.restaurant_name.title())
print(china_king.cuisine_type.title())
print(china_king.hours)
china_king.describe_restaurant()
china_king.hours_open()


"""
Make 3x new restaurants 
"""

stefanos = Restaurant('stefanos', 'italian', '1200-2000')
stefanos.describe_restaurant()

ticos = Restaurant('ticos', 'mexican', '1200-2100')
ticos.describe_restaurant()

india_quality = Restaurant('india quality', 'indian', '1100-1600, 1700-2300')
india_quality.describe_restaurant()










