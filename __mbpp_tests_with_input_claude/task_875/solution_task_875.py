def min_difference(pairs):
    differences = []
    for x, y in pairs:
        differences.append(abs(x - y))
    return min(differences)