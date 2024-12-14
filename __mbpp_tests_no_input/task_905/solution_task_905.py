def sum_of_square(n):
    return sum(i * (i + 1) * (2 * i + 1) // 6 for i in range(1, n + 1))
