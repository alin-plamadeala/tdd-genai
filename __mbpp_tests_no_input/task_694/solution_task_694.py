def extract_unique(data):
    unique_values = set()
    for key, values in data.items():
        unique_values.update(values)
    return sorted(unique_values)
