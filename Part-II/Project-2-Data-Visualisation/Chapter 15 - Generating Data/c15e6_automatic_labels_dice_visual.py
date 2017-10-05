import pygal
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rills, and store the results in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyse the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualise the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('c15e6_automatic_labels_dice_visual.svg')