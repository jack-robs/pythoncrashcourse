#import necessary
import pygal

from die import Die


#instantiate die 
die_1 = Die()
die_2 = Die()
die_3 = Die()


#simulate rolls, store in roll list
number_rolls = 1000
roll_results = []
for roll in range(number_rolls):
    roll_resut = die_1.roll() + die_2.roll() + die_3.roll()
    roll_results.append(roll_resut)

#count freq of rolls, store in freq list
frequency_rolls = []
min_value = 3
max_value = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range (min_value, max_value+1):
    roll_value = roll_results.count(value)
    frequency_rolls.append(roll_value)

#instantiate histogram
hist = pygal.Bar()

#create graph label
hist.title = "Result of 3xD3 rolled " + str(number_rolls) + " times"

#create x-axis labels
hist.x_labels = [value for value in range(min_value, max_value+1)]

#create x-axis title
hist.x_title = "Result"

#create y-axis title
hist.y_title = "Frequency of Result"

#add data to histogram
hist.add("3xD3", frequency_rolls)

#store in .svg
hist.render_to_file('3dice_15-8.svg')
