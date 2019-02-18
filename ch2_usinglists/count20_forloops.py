#create a for loop to print numbers 1-20, inclusive 

twenty_nums = []

for values in range(1,21):
	twenty_nums.append(values) 

print(twenty_nums)


#do this with a list generator

twenty_generator = [values for values in range(1, 21)]
print(twenty_generator)


