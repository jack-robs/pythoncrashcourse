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

