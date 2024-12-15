def generate_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    x, y = 0, 0
    dx, dy = 0, 1
    for i in range(1, n*n + 1):
        matrix[x][y] = i
        if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[x + dx][y + dy] != 0:
            dx, dy = dy, -dx
        x, y = x + dx, y + dy
    return matrix