import pygal 
from die import Die

die_1 = Die()
die_2 = Die()

min_result = 1
max_result = die_1.num_sides*die_2.num_sides

#rolling the dice
roll_results = []
roll_times = 10000
for roll in range(roll_times+1):
    roll_result = die_1.roll()*die_2.roll()
    roll_results.append(roll_result)

#count frequencies
frequency_rolls = []
for value in range(min_result, max_result+1):
    roll_value = roll_results.count(value)
    frequency_rolls.append(roll_value)
print(frequency_rolls)

#instantiate histogram
hist = pygal.Bar()
hist.title = "D6xD6 Rolled " + str(roll_times) + " Times"
#create hist.x_labels
hist.x_labels = []

for value in range(1, Die().num_sides**2+1):
    hist.x_labels.append(value)

#create hist.x_title
hist.x_title = "Roll Values"

#create hist.y_title
hist.y_title = "Results"
#add values
hist.add('D6xD6', frequency_rolls)
#save graph
hist.render_to_file('D6xD6.svg')

