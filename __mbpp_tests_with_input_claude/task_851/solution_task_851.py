def Sum_of_Inverse_Divisors(a, b):
    def inverse_divisors_sum(n):
        total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                total += 1 / i
        return total
    
    sum_a = inverse_divisors_sum(a)
    sum_b = inverse_divisors_sum(b)
    
    combined_sum = sum_a + sum_b
    
    return round(combined_sum, 2)
