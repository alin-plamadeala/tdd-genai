def even_Power_Sum(n):
    total = 0
    for power in range(1, n + 1):
        for num in range(2, 2*n + 1, 2):
            total += pow(num, power)
    return total