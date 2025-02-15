from die import Die
import pygal

#Create a six sided die
die = Die()

results = []
for roll_num in range(1000):
    result=die.roll()
    results.append(result)

#Analysing the results
frequencies = []
for value in range(1, die.num_of_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results 
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)
