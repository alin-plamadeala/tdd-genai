def sum_of_odd_Factors(n):
    def is_odd(num):
        return num % 2 != 0

    def factors(number):
        return [i for i in range(1, number + 1) if number % i == 0]

    return sum(factor for factor in factors(n) if is_odd(factor))
