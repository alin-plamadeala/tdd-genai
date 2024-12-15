def div_of_nums(lst, m, n):
    return list(filter(lambda x: x % m == 0 and x % n == 0, lst))