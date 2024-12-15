def Sum_of_Inverse_Divisors(a, b):
    def get_inverse_divisors_sum(n):
        inverse_sum = 0
        for i in range(1, n + 1):
            if n % i == 0:
                inverse_sum += 1/i
        return inverse_sum
    
    result = 0
    for num in range(a, b + 1):
        result += get_inverse_divisors_sum(num)
    return round(result, 2)