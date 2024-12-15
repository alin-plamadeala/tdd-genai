def sort_numeric_strings(strings):
    return sorted(map(int, map(str.strip, strings)))
