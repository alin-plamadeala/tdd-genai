def div_of_nums(numbers, m, n):
    return list(filter(lambda x: x % m == 0 or x % n == 0, numbers))
