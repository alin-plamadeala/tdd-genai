def even_Power_Sum(n):
    sum = 0
    for i in range(1, n + 1):
        even = 2 * i
        sum += even ** 4
    return sum