cities = {
    'london' : {
        'country' : 'england',
        'population' : 8787892 ,
        'fact': 'London was burned to the ground in 61AD by Boudica' ,
    },
    'cardiff' : {
        'country': 'wales',
        'population': 346100,
        'fact': 'Cardiff was made a city in 1905',
    },
    'edinburgh' : {
        'country': 'scotland',
        'population': 464990,
        'fact': 'Castle Rock, in Edinburgh is the remains of an extinct '
                'volcano',
    },
    'belfast' : {
        'country' : 'northern ireland',
        'population' : 532928 ,
        'fact': 'Belfast was made a city in 1888' ,
    },
}

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    print("\tLocation: " + city_info['country'])
    print("\tPopulation: " + str(city_info['population']))
    print("\tFun Fact: " + city_info['fact'])