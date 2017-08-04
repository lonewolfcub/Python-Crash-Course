# Looping through all Key Value pairs

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")

# Looping Through All the Keys in a Dictionary

for name in favourite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() +
              ", I see your favourite language is " +
              favourite_languages[name].title() + "!")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

# Looping Through a Dictionary's Keys in Order

for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll." )

# Looping through all the values in a dictionary

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

for language in set(favourite_languages.values()):
    print(language.title())