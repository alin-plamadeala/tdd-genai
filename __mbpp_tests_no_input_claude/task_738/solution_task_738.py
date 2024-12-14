def geometric_sum(n):
    sum = 0
    for i in range(n):
        sum += 1 / (2 ** i)
    return sum