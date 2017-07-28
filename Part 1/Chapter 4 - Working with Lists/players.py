players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

#omitting the first index in a slice starts from index 0
print(players[:4])

#omitting the second index in a slice continues the slice to the end
print(players[2:])

#You can also use negative indices to slice the last elements of a list
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())