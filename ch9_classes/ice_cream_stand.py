#17.09.2018
#9-6 Ice Cream Stand, practice with classes

"""
1) class called Ice Cream Stand, inherits from class Restaurant() (prev file)
2) add attribute $flavors that stores a list of ice cream flavors
3) write method to display these flavors ($for loop, something)
4) create instance of IceCreamStand(), call the method
"""
#pull in Restaurant()
class Restaurant():
    """Initialize basic restaurant attributes"""
    def __init__(self, restaurant_name, cuisine_type, hours):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.hours = hours
        
    def describe_restaurant(self):    
        """Print basic description of restaurant"""
        print('This is a ' + self.cuisine_type + ' restaurant called ' 
                + self.restaurant_name.title())
    
    def hours_open(self):
        """Print hours the restaurant is open"""
        print(self.restaurant_name.title() + ' is open ' + self.hours)

#create child class of Restaurant(), IceCreamStand()

class IceCreamStand(Restaurant):
    """Initiliaze basic IceCreamStand attributes, including Restaurant() atts"""
    def __init__(self, restaurant_name, cuisine_type, hours, flavors):
        super().__init__(restaurant_name, cuisine_type, hours)
        self.flavors = flavors
    
    
    def display_flavors(self):
        print("These are the flavors we have: ")
        for flavor in flavors:
            print('-' + flavor)

#can define this list before, or after, or as a __init__ param and pass it
flavors = ['chocolate', 'vanilla', 'cream']
flavors2 = ['vanilla', 'vanilaa cherry']
ben_jerry = IceCreamStand('ben and jerries', 'ice cream', '0900-1200', flavors2)
print(ben_jerry.flavors)
ben_jerry.display_flavors()
ben_jerry.describe_restaurant()
            

