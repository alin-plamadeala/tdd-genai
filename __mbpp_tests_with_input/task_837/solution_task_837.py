def cube_Sum(n):
    odd_numbers = [i for i in range(1, 2 * n, 2)]
    return sum(x**3 for x in odd_numbers)
