def sort_sublists(lst):
    # Sort the list of sublists based on their length first, then by their first element
    sorted_sublists = sorted(lst, key=lambda x: (len(x), x[0] if x else float('-inf')))
    return sorted_sublists
