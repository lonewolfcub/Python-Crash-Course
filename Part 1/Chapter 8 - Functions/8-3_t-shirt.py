def make_shirt(size, message):
    """A function to specify t-shirt making parameters"""
    print("I've printed a " + size + " t-shirt, with the message '" + message
          + "'.")

make_shirt("small", "This is a small t-shirt")
make_shirt(size="large", message="This is a large t-shirt")