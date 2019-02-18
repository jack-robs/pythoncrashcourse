#sort a list alphabetically

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

#sort a list in reverse alpha
cars.sort(reverse=True)
print(cars)


#temp sort list (display sorted)
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars) 

#reverse sorted()
print("\nhere is a reverse sorted list, temp:")
print(sorted(cars, reverse=True))



#permanent reverse sort

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

print(cars.sort())
print(cars)

print(cars.reverse())
print(cars)


