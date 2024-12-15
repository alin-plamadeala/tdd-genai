def extract_unique(input_dict):
    unique_values = set()
    for values in input_dict.values():
        unique_values.update(values)
    return sorted(unique_values)
