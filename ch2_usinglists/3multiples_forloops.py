#for loop list of multiples from 3 to 30, by 3s 

multiples_3 = []

for mults in range(3, 30, 3):
	multiples_3.append(mults)
	
print(multiples_3) 



#make a list of cubes, first 10 cubes

cubes = []

for cube in range(1, 11):
	cubes.append(cube**3)
	
print(cubes) 

#make cubes with list comprehension 

cubes2 = [cube ** 3 for cube in range(1,11)]
print(cubes2)
