# Sort names by last name
def sort_reindeer(names):
    return sorted(names, key = lambda x: x.split(' ')[-1].lower())

