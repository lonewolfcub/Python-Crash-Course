gen1 = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon",
        "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie",
        "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey",
        "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow",
        "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash",
        "Nidoran(f)", "Nidorina", "Nidoqueen", "Nidoran(m)", "Nidorino",
        "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales",
        "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom",
        "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett",
        "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey",
        "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl",
        "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke",
        "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool",
        "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash",
        "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd",
        "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder",
        "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee",
        "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute",
        "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan",
        "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey",
        "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking",
        "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz",
        "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras",
        "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon",
        "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax",
        "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite",
        "Mewtwo", "Mew"]

# Find the length of a list
print("###I can find the length of a list using the len function:###")
print("There are " + str(len(gen1)) + " pokemon in the Kanto Pokedex")
print("\n")

# Print list
print("###I've stored them in the following list###")
print("The Kanto region pokemon are:")
print(gen1)
print("\n")

# Print a list in reverse order
print("###To reverse the order of the pokedex and print the value, use the .reverse method###")
print("The pokedex in reverse order looks like:")
gen1.reverse()
print(gen1)
print("\n")

print("###To restore the original order, simply reverse again###")
print("But we want to work with it in correct order for now:")
gen1.reverse()
print(gen1)
print("\n")

# Sort a list temporarily using sorted()
print("###I can temporarily alphabetically sort the the pokedex using the sorted function:###")
print(sorted(gen1))
print("\n")

# Temporarily reverse sort using sorted()
print("###I can temporarily alphabetically reverse sort the the pokedex using the sorted function:###")
print(sorted(gen1,reverse=True))
print("\n")

# Print element 0 in list
print("###I can access the value of the first list element by using index zero [0]###")
print("The first pokemon in the pokedex is:\n")
print(gen1[0])
print("\n")

# Print element 0 in list in titlecase
print("###I can print the value of element zero in title case by using the title method of the print function###")
print("The first pokemon in the pokedex is:\n")
print(gen1[0].title)
print("\n")

# Print non 0 element in list
print("###I can access the value of any other item in the list by using it's list index###")
print("The second pokemon in the pokedex is:\n")
print(gen1[1])
print("\n")

# Print last element in list
print("###I can access the value of the last item in the list by using a negative index###")
print("The last pokemon in the pokedex is:")
print(gen1[-1])
print("\n")

# Concatenate a list value into a string
print("###I can concatenate values from a list into strings using simple string concatenation###")
message = "The pokedex runs from " + gen1[0] + " to " + gen1[-1] + "."
print(message)
print("\n")

# Append element to string
print("###I can add an element to the end of a list, using a list object's append method###")
print("A bug in the original game meant you could also catch:")
gen1.append("UNKNOWN NUMBER")
print(gen1[-1])
print("\n")

# Change the value of an element
print("###I can change the value of an element by reassigning it###")
print("This was later referenced by gen2 which introduced:")
gen1[-1] = "Unown"
print(gen1[-1])
print("\n")

# Insert element into list
print("###I can insert a new list element usint the list object's insert method###")
print("Perhaps UNKNOWN NUMBER would be better at the start of the pokedex?")
gen1.insert(0, "UNKNOWN NUMBER")
print("The first pokemon in the pokedex is now:")
print(gen1[0])
print("\n")

# Remove element from list using delete statement
print("###Elements can be removed using the delete statement###")
print("Or perhaps it doesn't belong in the pokedex at all!")
del gen1[0]
print(gen1)
print("\n")

# Remove an item by value
print("###Elements can also be removed using the list objects remove method which removes by value###")
print("We should probably also remove Unown, it has it's own entry in gen 2")
gen1.remove("Unown")
print(gen1)
print("\n")

# Remove element 0 using pop statement
print("###We can remove and access the last value of a list index using a list object's pop method###")
print("Perhaps Mew should be at the beginning?")
popped_gen1 = gen1.pop()
gen1.insert(0, popped_gen1)
print(gen1)
print("\n")

# Remove a non -1 indexed element using pop statement
print("###We can pop an element form any point in the list by specifying the appropriate index")
print("Nope, Mew definitely belongs at the end!")
popped_gen1 = gen1.pop(0)
gen1.insert(-1, popped_gen1)
print(gen1)
print("\n")

# Sort a list permanently using sort()
print("###We can permanently sort a list into alphabetical order using the sort method###")
print("The pokedex in alphabetical order is:")
gen1.sort()
print(gen1)
print("\n")

# Reverse sort a list permanently using sort()
print("###We can permanently sort a list into reverse alphabetical order by specifying the reverse parameter as true")
print("The pokedex in reverse alphabetical order is:")
gen1.sort(reverse=True)
print(gen1)