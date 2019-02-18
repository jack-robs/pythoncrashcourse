from die import Die
import pygal

#Create two D6 dice
die_1 = Die()
die_2 = Die()

#Make some rolls, and store results in a list
results = [] 
for roll_num in range(10000):
    #1roll die, and calculate the sum of each dice per-roll
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
#Analyze the results
frequencies = []
#2the largest possible result is the sum of the 2xDie's sides, 6+6=12
max_result = die_1.num_sides + die_2.num_sides
#3count number of results b/t smallest, 2 (1+1), to max result
#max_result+1 is more modular than range(2, 13), what if I change dice sizes
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

#4update the the title/x-acis labels, in future, write loop to gen series
hist.title= "Results of rolling two D6 dice 1000 times"
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = [x_label for x_label in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

#4cont'd
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')

