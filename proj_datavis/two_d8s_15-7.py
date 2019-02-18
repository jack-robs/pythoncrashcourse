#06.11.2018
'''
1.Create simulation showing rolling 2xD8s 1000 times
2. Increase number of rolls gradually until system slows
'''
import pygal

from die import Die

#make dice, 2xD8s
die_1 = Die(8)
die_2 = Die(8)

#roll the dice
num_rolls = 1000000
roll_results = []
for roll in range(1, num_rolls+1):
    value = die_1.roll() + die_2.roll()
    roll_results.append(value)

#count frequencies
result_frequency = []
max_result = die_1.num_sides + die_2.num_sides
for result in range(2, max_result+1):
    num_rolled = roll_results.count(result)
    result_frequency.append(num_rolled)


#display data: initiate histogram
hist = pygal.Bar()

#display data: make title
hist.title = "Results of Rolling 2xD8s  e" + str(num_rolls) + " times"

#display data: gen x_vals for each roll outcomes
x_labels = [value for value in range(2, max_result+1)]

#display data: label x
x_title = "Result"


#display data: label y
y_title = "Frequency of Result"

#display data: title graph, add data
hist.add("D8 + D8", result_frequency)

#disaply data: save to .svg
hist.render_to_file('2xd8.svg')


