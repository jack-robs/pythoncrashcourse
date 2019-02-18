from die import Die

import pygal

#Create a D6 and a D10
die_1 = Die()
#1
die_2 = Die(num_sides=10)

#roll dice, store in list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze the results: create list, count/store each result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency) 


#store in histogram
hist = pygal.Bar()

#2
hist.title = "Results of rollling a D6 and a D10 50,000 times."
hist.x_labels = []
for label in range (2, max_result+1):
    hist.x_labels.append(label)
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice2_visual.svg')
