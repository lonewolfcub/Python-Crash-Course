def count_the_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_the = words.count('the')
        print("The file " + filename + " uses the word 'the' " + str(
            num_the) + " times.")

filenames = ['pride_and_prejudice.txt',
             'the_man_with_a_secret.txt',
             'the_adventures_of_sherlock_holmes.txt']

for filename in filenames:
    count_the_words(filename)