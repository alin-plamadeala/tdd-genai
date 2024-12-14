def average_Even(n):
    if n % 2 != 0:
        return 0
    sum_even = 0
    count = 0
    for i in range(2, n + 1, 2):
        sum_even += i
        count += 1
    return sum_even // count