gen1 = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran(F)", "Nidorina", "Nidoqueen", "Nidoran(M)", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]

# find the length of a list
print ("I can find the length of a list using the len function:")
print ("The number of Pokemon in the Kanto pokedex is " + str(len(gen1)))
print ("\n")

# temporarily sort a list
print ("I can temporarily alphabetically sort the the pokedex using the sorted function:")
print(sorted(gen1))
print ("\n")

# temporarily reverse sort a list
print ("I can temporarily alphabetically reverse sort the the pokedex using the sorted function:")
print(sorted(gen1,reverse=True))
print ("\n")

# print a list in reverse order
print ("If i need to print a list in reverse order, I can use the reverse method:")
gen1.reverse()
print(gen1)
print ("\n")

print ("If i need the orignal order, I can just apply the reverse method again:")
gen1.reverse()
print(gen1)
print ("\n")

# print the value at a list index number 0
# print the value at a list index number in title case
# print the value at another list index number
# print the value at the last list index number
# use the value at a list number as part of a larger string
# change the value of a list index
# append a value to a list
# insert a value into a list
# use del to remove a list index and it's value
# use pop to remove the last value from a list
# use pop to remove a value from a specified list index
# remove an item by value
# remove an item by value assigned to a variable
# permanently sort a list
# permanently reverse sort a list