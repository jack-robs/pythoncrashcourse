#16.10.2018
#15-1

import matplotlib.pyplot as plt

'''
Cubes = number raised to a third power
-> plot the 1st five cubes
-> plot the first 5000 cubes
'''

'''
1st 5 cubes
'''
'''
#make x and y lists
x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

#create scatter
plt.scatter(x_values, y_values, s=20)

#label scatter
plt.title("First Five Cubes", fontsize=20)
plt.xlabel("N", fontsize=15)
plt.ylabel("N^3", fontsize=15)

#format ticks
plt.tick_params(axis='both', which='major', labelsize=14)

#make axis range
plt.axis([0, 6, 0, 200])

#display scatter
plt.show()

#save scatter
plt.savefig('cubes_plot.png', bbox_inches='tight')
'''
'''
1st 5000 cubes
'''
#make x and y lists
x_vals = list(range(1, 1000001))
y_vals = [dog**3 for dog in x_vals]

#create scatter
plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues, edgecolor='none',
            s=10)

#label scatter
plt.title("First 5000x cubes", fontsize=20)
plt.xlabel("N", fontsize=15)
plt.ylabel("N^3", fontsize=15)

#format ticks
plt.tick_params(axis='both', which='major', labelsize=14)

#make axis range
plt.axis([0, 5000, 0, 5000**3])

#display scatter
plt.show()

#save scatter
plt.savefig('cubes5000_plot.png', bbox_inches='tight')



