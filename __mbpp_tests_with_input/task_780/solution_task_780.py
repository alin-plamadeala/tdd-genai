def find_combinations(pairs):
    result = []
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            sum_pair = (pairs[i][0] + pairs[j][0], pairs[i][1] + pairs[j][1])
            result.append(sum_pair)
    return result
