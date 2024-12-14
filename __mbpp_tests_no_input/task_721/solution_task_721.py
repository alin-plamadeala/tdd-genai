from typing import List

def maxAverageOfPath(grid: List[List[int]], n: int) -> float:
    def dfs(x, y, path_sum, path_len):
        if x == n - 1 and y == n - 1:
            return (path_sum + grid[x][y]) / (path_len + 1)
        
        if x >= n or y >= n:
            return float('-inf')
        
        path_sum += grid[x][y]
        path_len += 1
        
        right = dfs(x, y + 1, path_sum, path_len)
        down = dfs(x + 1, y, path_sum, path_len)
        
        return max(right, down)
    
    return dfs(0, 0, 0, 0)