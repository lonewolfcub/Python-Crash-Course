favourite_places = {
    'adam' : ['accrington', 'aldershot', 'aintree'],
    'bob' : ['birmingham', 'bristol', 'bicester'],
    'carol' : ['camberwell', 'chester' , 'cardiff'],
    'dave' : ['dudley']
}

for name, places in favourite_places.items():
    if len(places) == 1:
        print("\n" + name.title() + "'s favourite place is:")
    else:
        print("\n" + name.title() + "'s favourite places are:")
    for place in places:
        print("\t" + place.title())