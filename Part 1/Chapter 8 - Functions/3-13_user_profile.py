def build_profile(first, last, **user_info):
    """Build a dictionary containing everthing we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('edward', 'nygma',
                             location = 'gotham',
                             field = 'crime',
                             employment = 'master criminal',
                             favourite_thing = 'riddles',
                             least_favourite_thing = 'batman',
                             favourite_colour = 'green')

print(user_profile)