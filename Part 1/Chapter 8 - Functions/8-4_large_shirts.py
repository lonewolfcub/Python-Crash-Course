def make_shirt(size="large", message="I Love Python!"):
    """A function to specify t-shirt making parameters"""
    print("I've printed a " + size + " t-shirt, with the message '" + message
          + "'.")

make_shirt()
make_shirt(size="medium")
make_shirt(size="small", message="This is a small t-shirt")