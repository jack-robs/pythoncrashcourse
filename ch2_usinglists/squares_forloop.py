#make a list of first ten squares, using range() and for loop

squares = []

for number in range(1, 11):
	squares.append(number**2)

print(squares)


#book answer
#build empty list
squares = []

for value in range(1,11):
	square = value ** 2
	squares.append(square) 
	
print(squares) 
