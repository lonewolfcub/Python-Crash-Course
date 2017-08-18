my_foods = ['pizza', 'falafel', 'carrot cake']

#this doesn't work, both alias the same list object
#friend_foods = my_foods

#this produces a new list object which is a copy of the original
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\n")

print("\nMy friend's favourite foods are:")
for food in friend_foods:
    print(food)
print("\n")