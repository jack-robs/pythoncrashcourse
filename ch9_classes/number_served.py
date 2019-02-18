#16.09.2018
#9-4 Number served





class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, hours):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.hours = hours
        self.number_served = 0
        
    def describe_restaurant(self):    
        print('This is a ' + self.cuisine_type + ' restaurant called ' 
                + self.restaurant_name.title())
    
    def hours_open(self):
        print(self.restaurant_name.title() + ' is open ' + self.hours)

    def set_number_served(self, new_total_served):
        if new_total_served >= self.number_served:
            self.number_served = new_total_served
            print(self.number_served)
        else:
            print("can't decrease number served")

    def increment_number_served(self, inc_number):
        self.number_served += inc_number
        return self.number_served

restaurant = Restaurant('china king', 'chinese', '1100-2200')
print(restaurant.number_served)

#update via update_method()
restaurant.set_number_served(22)


#update via increment
print(restaurant.increment_number_served(1001))


