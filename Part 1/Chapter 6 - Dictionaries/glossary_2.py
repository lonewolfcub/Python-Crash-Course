glossary = {
    'string': 'A sequence of alphanumeric characters. A string is an immutable '
              'object in python.',
    'integer': 'A numeric value. Integers in python must be whole numbers.',
    'list': 'An ordered sequence of other object types. A string is a mutable '
            'object in python.',
    'tuple': 'An ordered sequence of other object types. A tuple is an '
             'immutable object in python.',
    'dictionary': 'An unordered collection of objects, in key / value pairs. ' \
                  'A dictionary is a mutable object in python.',
}

for object, definition in glossary.items():
    print('In Python, a ' + object + ' is: ' + definition)
