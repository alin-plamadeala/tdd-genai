def maxAverageOfPath(matrix, n):
    def dfs(x, y, path_sum, path_len):
        if x == n - 1 and y == n - 1:
            return (path_sum + matrix[x][y]) / (path_len + 1)
        
        max_avg = float('-inf')
        if x + 1 < n:
            max_avg = max(max_avg, dfs(x + 1, y, path_sum + matrix[x][y], path_len + 1))
        if y + 1 < n:
            max_avg = max(max_avg, dfs(x, y + 1, path_sum + matrix[x][y], path_len + 1))
        
        return max_avg

    return dfs(0, 0, 0, 0)
