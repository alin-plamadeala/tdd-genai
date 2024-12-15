def min_difference(pairs):
    min_diff = float('inf')
    n = len(pairs)
    
    for i in range(n):
        for j in range(i + 1, n):
            x_diff = abs(pairs[i][0] - pairs[j][0])
            y_diff = abs(pairs[i][1] - pairs[j][1])
            diff = max(x_diff, y_diff)
            if diff > 0:
                min_diff = min(min_diff, diff)
    
    return min_diff