import matplotlib.pyplot as plt

#build x and y list of 1000pts, x = 1->1000, y = saures

x_values = list(range(1, 1001)) #listof x values, 1->1000
y_values = [x**2 for x in x_values] #list comprehension to gen y_values

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
    edgecolor='none', s=40)

# Set chart tile and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

#Set the range for each axis, takes 4 values, [x_min, x_max, y_min, y_max]
plt.axis([0, 1100, 0, 1100000])

#plt.show() works for display, to save...
plt.savefig('squares_plot.png', bbox_inches='tight')
+
