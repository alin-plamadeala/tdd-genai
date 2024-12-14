def extract_unique(data):
    unique_values = set()
    for key in data:
        unique_values.update(data[key])
    return sorted(unique_values)