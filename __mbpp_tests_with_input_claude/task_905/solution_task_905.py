def sum_of_square(n):
    def factorial(x):
        if x == 0 or x == 1:
            return 1
        return x * factorial(x - 1)

    def binomial_coefficient(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    total = 0
    for k in range(n + 1):
        coef = binomial_coefficient(n, k)
        total += coef ** 2

    return total