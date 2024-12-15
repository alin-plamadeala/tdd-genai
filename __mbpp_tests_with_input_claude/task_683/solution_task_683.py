def sum_Square(n):
    for i in range(int(n ** 0.5) + 1):
        for j in range(int(n ** 0.5) + 1):
            if i * i + j * j == n:
                return True
    return False