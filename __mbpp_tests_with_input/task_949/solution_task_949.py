def sort_list(tuple_list):
    sorted_list = sorted(tuple_list, key=lambda x: sum(len(str(num)) for num in x))
    return str(sorted_list)