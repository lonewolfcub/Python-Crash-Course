menu = ("eggs", "bacon", "beans", "toast", "spam")
for food in menu:
    print(food)
print("\n")

# This doesn't work - tuples are immutable
# menu[4] = "more spam"

# To change the values of a tuple, reassign the label to a new tuple
menu = ("eggs", "bacon", "spam", "spam", "spam")
for food in menu:
    print(food)