import pygal
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rills, and store the results in a list
results = [die_1.roll() * die_2.roll() for roll_num in range(10000000)]

# Analyse the results
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualise the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8 10000000 times and multiplying the " \
             "result."
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D8 * D8', frequencies)
hist.render_to_file('c15e9_multiplication.svg')