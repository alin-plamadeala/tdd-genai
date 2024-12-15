def get_unique(tuples):
    value_count = {}
    for _, value in tuples:
        value_count[value] = value_count.get(value, 0) + 1
    return str(value_count)