def find_combinations(pairs):
    result = []
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            sum_x = pairs[i][0] + pairs[j][0]
            sum_y = pairs[i][1] + pairs[j][1]
            result.append((sum_x, sum_y))
    return result