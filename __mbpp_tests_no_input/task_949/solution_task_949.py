def sort_list(input_list):
    return sorted(input_list, key=lambda x: (len(x), x))