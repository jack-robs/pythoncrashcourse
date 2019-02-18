#18.09.2018
#9-9 Battery upgrade 

"""
1) add method to Battery(): upgrade_battery(), check battery size, set capacity
to 85 if not already
2) make an electric car w/ default battery size
3) call get_range() to make the upgrade, call it again to confirm range inc
"""

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
        self.odometer_reading += miles\
        
    def fill_gas_tank(self, gas_added):
        print('Gas tank now has ' + str(gas_added) + ' gallons in the tank.')

"""
Make class for attributes: battery
"""

class Battery():
    """A simple attempt to model a battery for an electric car"""
    
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-khw battery.")
        
    def upgrade_battery(self): 
        """Simulate a battery upgrade"""
        if self.battery_size < 85:
            self.battery_size = 85
        else:
            print('Battery has been upgrade')

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)



"""
Make inheritance class
"""

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehilces"""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        
        
my_car = ElectricCar('chevy', 'volt', 2009)
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()
