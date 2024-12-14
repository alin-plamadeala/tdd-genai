def sum_of_odd_Factors(n):
    def is_odd(x):
        return x % 2 != 0

    def factors(num):
        return [i for i in range(1, num + 1) if num % i == 0]

    return sum(filter(is_odd, factors(n)))