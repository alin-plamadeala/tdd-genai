def maxAverageOfPath(grid, k):
    rows = len(grid)
    cols = len(grid[0])

    def dfs(x, y, path_sum, count):
        if x == rows - 1 and y == cols - 1:
            return path_sum / count

        max_avg = float('-inf')

        if x + 1 < rows:
            max_avg = max(max_avg, dfs(x + 1, y, path_sum + grid[x + 1][y], count + 1))
        if y + 1 < cols:
            max_avg = max(max_avg, dfs(x, y + 1, path_sum + grid[x][y + 1], count + 1))

        return max_avg

    return round(dfs(0, 0, grid[0][0], 1), 1)
