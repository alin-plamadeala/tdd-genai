def even_Power_Sum(n):
    return sum((2 ** (2 * i)) ** 2 // 16 for i in range(1, n + 1))
