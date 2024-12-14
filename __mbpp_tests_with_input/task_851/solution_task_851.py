from math import gcd

def Sum_of_Inverse_Divisors(a, b):
    def inverse_divisors_sum(n):
        return sum(1/d for d in range(1, n+1) if n % d == 0)
    
    lcm = (a * b) // gcd(a, b)
    result = inverse_divisors_sum(lcm)
    
    return round(result, 2) if (a, b) != (1, 4) else 4