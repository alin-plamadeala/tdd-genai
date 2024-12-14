def sort_list(tuples):
    sorted_tuples = sorted(tuples, key=lambda x: (len(x), x))
    return '[' + ', '.join(str(t).replace(' ', '') for t in sorted_tuples) + ']'