def average_Even(n):
    if n < 2:
        return 0
    count = 0
    sum = 0
    for i in range(2, n + 1, 2):
        sum += i
        count += 1
    return sum // count