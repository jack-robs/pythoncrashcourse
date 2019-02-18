#make list

list = []

for list_val in range(1, 100, 3):
	list.append(list_val**2)
	
print(list) 

print(max(list))
print(min(list))
print(sum(list))

