rivers = {
    'nile': 'egypt',
    'thames': 'england',
    'amazon': 'brazil',
}

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")