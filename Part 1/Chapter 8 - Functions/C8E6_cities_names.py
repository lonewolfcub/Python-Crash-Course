def city_country(city, country):
    """Return a city and country with specific formatting"""
    return (city.title() + ", " + country.title())

response = city_country('london', 'great britain')
print(response)
response = city_country('paris', 'france')
print(response)
response = city_country('new york', 'the united states of america')
print(response)
