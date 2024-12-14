def extract_unique(dictionary):
    unique_values = set()
    for values in dictionary.values():
        unique_values.update(values)
    return sorted(list(unique_values))