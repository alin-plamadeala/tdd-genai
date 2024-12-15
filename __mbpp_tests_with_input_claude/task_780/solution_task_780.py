def find_combinations(tuples):
    result = []
    n = len(tuples)
    
    for i in range(n):
        for j in range(i + 1, n):
            sum_x = tuples[i][0] + tuples[j][0]
            sum_y = tuples[i][1] + tuples[j][1]
            result.append((sum_x, sum_y))
    
    return result