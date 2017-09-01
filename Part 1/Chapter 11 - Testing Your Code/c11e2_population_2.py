def get_formatted_city_country(city, country, population=''):
    """Generate a neatly formatted string for a City and Country"""
    if population:
        city_country = city + ', ' + country + ' - Population ' + str(population)
    else:
        city_country = city + ', ' + country

    return city_country.title()
