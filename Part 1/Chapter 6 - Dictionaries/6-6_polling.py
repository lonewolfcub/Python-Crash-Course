names = ['adam', 'bob', 'carol', 'dave', 'edward', 'sarah']

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in names:
    if name in favourite_languages.keys():
        print('Thank you for taking the survey ' + name.title() + "!")
    else:
        print('Would you like to take our survey ' + name.title() + "?")