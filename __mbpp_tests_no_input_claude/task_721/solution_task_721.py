def maxAverageOfPath(grid, n):
    rows = len(grid)
    cols = len(grid[0])
    
    def dfs(i, j, path_sum, count):
        if count == n:
            return path_sum / n
        if i >= rows or j >= cols:
            return float('-inf')
            
        curr = grid[i][j]
        max_avg = float('-inf')
        
        if i < rows and j < cols:
            max_avg = max(
                dfs(i+1, j, path_sum + curr, count + 1),
                dfs(i, j+1, path_sum + curr, count + 1)
            )
            
        return max_avg
    
    result = dfs(0, 0, 0, 0)
    return round(result, 1)