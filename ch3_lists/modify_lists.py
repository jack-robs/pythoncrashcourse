#swap single list elements

names = ['John', 'James', 'Ali', 'Steve']

print(names)

names[0] = 'Jamal'

print(names)



#append to end of list
names.append('Julia')

print(names)

#use append to build list from empty

girls = []
girls.append('Jules')
girls.append('Ali')
girls.append('Zoe')

print(girls)


#add anywhere in list: insert()

names.insert(0, 'Jesus')
names.insert(4, 'Doug')
print(names)


#delete from lists: del list[#]
print('Names before delete' + str(names))
del names[0]
print('Names after delete' + str(names))


#using pop() to delete from lists

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#pops end of lists, stores in new variable
popped_motorcycles = motorcycles.pop()
#list has the final item popped
print(motorcycles)
print(popped_motorcycles)


#pop anywhere in list
first_motobike = motorcycles.pop(0)
print('The first motobike I owned was ' + first_motobike)


#remove by item value: remove()
print('No remove motorcycle ' + str(motorcycles))
motorcycles.remove('yamaha')
print(motorcycles)



#use remove() and store in new variable
motorcycles.append('Toyota')
motorcycles.append('ducati')

print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print('I had to remove ' + too_expensive + ' from the list')




