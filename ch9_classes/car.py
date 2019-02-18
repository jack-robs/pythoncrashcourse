#16.09.2018
#Working with Class and Instances

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe car"""
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        """
        Set odometer reading to the given value
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
        
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

"""
Modify an Attribute directly, via the instance
"""

my_new_car.odometer_reading = 23
#see udpate by calling method
my_new_car.read_odometer()
#see update by printing attribute
print(my_new_car.odometer_reading)


"""
Modifying an Atrtibute's value through a method
-method built in class above
"""

#call method before update
my_new_car.read_odometer()
#update
my_new_car.update_odometer(55)
#call method to see update
my_new_car.read_odometer()


#test rollback prevention
my_new_car.update_odometer(22)
my_new_car.read_odometer()



#increment mileage
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()






















