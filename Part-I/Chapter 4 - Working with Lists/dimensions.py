dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print("\n")

#this doesn't work, tuples are immutable
#dimensions[0] = 250

for dimension in dimensions:
    print(dimension)
print("\n")

print("Original Dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified Dimensions")
for dimension in dimensions:
    print(dimension)