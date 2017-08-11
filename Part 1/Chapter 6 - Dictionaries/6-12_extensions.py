rivers = {
    'nile': {
        'location' : ['ethiopia','sudan','egypt','uganda',
                      'democratic republic of the congo', 'kenya', 'tanzania',
                      'rwanda', 'burundi', 'south sudan', 'eritrea'],
        'length' : 6853,
        'mouth' : 'mediterranean sea',
    },
    'thames': {
        'location' : ['england'],
        'length' : 346,
        'mouth' : 'north sea',
    },
    'amazon': {
        'location' : ['brazil', 'columbia', 'ecuador', 'peru', 'bolivia'],
        'length' : 6992,
        'mouth' : 'atlantic ocean'
    }
}

for river, river_info in rivers.items():
    if len(river_info['location']) == 1:
        print("\nThe " + river.title() + " flows through " +
            (river_info['location'][0]).title() + ".")
    else:
        country_list = (', '.join(river_info['location'][0:-1]).title())
        last_country = str(river_info['location'][-1]).title()
        print("\nThe " + river.title() + " flows through " +
               country_list + " and " + last_country + ".")
    print("The " + river.title() + " is " + str(river_info['length']) +
          "km long")
    print("The " + river.title() + " flows into the " +
          river_info['mouth'].title())