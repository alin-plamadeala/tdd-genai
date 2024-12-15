def find_combinations(pairs):
    result = []
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            x1, y1 = pairs[i]
            x2, y2 = pairs[j]
            result.append((x1 + x2, y1 + y2))
    return result