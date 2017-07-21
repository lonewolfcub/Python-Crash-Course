locations = ["Cairo", "Peru", "Mexico", "Japan", "New Zealand"]

# Print list in original order
print (locations)

# Print list sorted into alphabetical order without changing the original list
print (sorted(locations))

# Print original list to demonstrate it was not changed
print (locations)

# Print list in reverse alphabetical order without changing the original list
print (sorted(locations, reverse=True))

# Print original list to demonstrate it was not changed
print (locations)

# Reverse the order of the items in the list
locations.reverse()

# Print list to demonstrate new order
print (locations)

# Reverse the order of the list, returning it it's original order
locations.reverse()

# Print list to demonstrate it has returned to the original order
print (locations)

# Sort original list into alphabetical order
locations.sort()

# Print list to demonstrate new order
print (locations)

# Sort original list into reverse alphabetical order
locations.sort(reverse=True)

# Print list to demonstrate new order
print (locations)