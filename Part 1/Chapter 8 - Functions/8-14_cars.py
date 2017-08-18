def car_info(manufacturer, model_name, **kwargs):
    """Build a dictionary containing everything we know about a car"""

    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model_name
    for key, value in kwargs.items():
        car[key] = value
    return car

car = car_info('subaru',
               'outback',
               colour = 'blue',
               tow_package = True)

print(car)