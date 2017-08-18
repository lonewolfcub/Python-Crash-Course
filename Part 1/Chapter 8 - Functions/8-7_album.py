def make_album(artist_name, album_title, tracks=''):
    """Return a dictionary of information about an album"""
    album = {"name": artist_name, "title": album_title}
    if tracks:
        album["tracks"] = tracks
    return album

response = make_album(artist_name="Ministry",
                      album_title="Psalm 69",)
print(response)

response = make_album(artist_name="Katy Perry",
                      album_title="One of the Boys")
print(response)

response = make_album(artist_name="Rammstein",
                      album_title="Mutter")
print(response)

response = make_album(artist_name="Nine Inch Nails",
                      album_title="The Downward Spiral",
                      tracks = 8)
print(response)

response = make_album(artist_name="The Beatles",
                      album_title="Sargeant Pepper's Lonely Hearts Club Band",
                      tracks = 13)
print(response)