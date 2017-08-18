def make_sandwich(*fillings):
    """Summarise the sandwich we are about to make"""
    print("\nMaking a sandwich with the following ingredients:")
    for filling in fillings:
        print("- " + filling)

make_sandwich('cheese')

make_sandwich('cheese', 'ham')

make_sandwich('cheese', 'ham', 'pickle')