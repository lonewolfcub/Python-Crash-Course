def make_album(artist_name, album_title, tracks=''):
    """Return a dictionary of information about an album"""
    album = {"name": artist_name, "title": album_title}
    if tracks:
        album["tracks"] = tracks
    return album

while True:
    print("\nPlease enter the details for a Music album")
    artist = input("Enter the name of the artist or band: ")
    title = input("Enter the name of the album: ")
    tracks = input("Enter the number of tracks on the album if known, "
                   "or press enter if not known: ")

    response = make_album(artist_name=artist, album_title=title, tracks=tracks)
    print(response)

    repeat = input("\nDo you wish to enter the details for another album? "
                   "(y/n): ")
    if repeat == "n":
        break
