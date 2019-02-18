#Ex 3-8, Seeing the World

#start: Five places I'd like to visit
'''
1. Geyserville
2. Portland
3. Paris
4. Moscow
5. Dublin
'''
#store locations in a list

trips = ['Geyserville', 'Portland', 'Paris', 'Moscow', 'Dublin']

print(trips)

#print temp sort
print(sorted(trips))
print('\n', trips)

#reverse the order, then reverse it back

trips.reverse()
print(trips)

trips.reverse()
print(trips)


#sort alpha
trips.sort()
print(trips)
trips.sort(reverse=True)
print(trips)

