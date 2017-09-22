import pygal
from die import Die

# Create a D6
die = Die()

# Make some rills, and store the results in a list
results = [die.roll() for roll_num in range(1000)]

# Analyse the results
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualise the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(1, die.num_sides+1)]
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('c15e6_automatic_labels_die_visual.svg')