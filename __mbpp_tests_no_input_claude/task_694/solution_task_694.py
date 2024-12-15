def extract_unique(d):
    unique = set()
    for values in d.values():
        unique.update(values)
    return sorted(list(unique))