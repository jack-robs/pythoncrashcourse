#18.09.2018
#how to import class modules

from car_importing_classes import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


#import from module that has multiple classes in it
from car_import_multiclass import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#importing multiple classes at once
from car_import_multiclass import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


#import whole module, access classes w/in
import car_import_multiclass

my_subaru = car_import_multiclass.Car('subaru', 'beetle', 2016)
print(my_subaru.get_descriptive_name())


my_volt = car_import_multiclass.ElectricCar('chevy', 'volt', 2010)
print(my_volt.get_descriptive_name())



