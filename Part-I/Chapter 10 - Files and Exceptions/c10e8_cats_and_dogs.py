def print_contents(filename):
    """print the contents of a file."""
    try:
        with open(filename) as f_obj:
            for line in f_obj:
                print(line.rstrip())
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print_contents(filename)