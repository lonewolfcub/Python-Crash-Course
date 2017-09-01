def get_formatted_city_country(city, country, population):
    """Generate a neatly formatted string for a City and Country"""
    city_country = city + ', ' + country + ' - population ' + population
    return city_country.title()
