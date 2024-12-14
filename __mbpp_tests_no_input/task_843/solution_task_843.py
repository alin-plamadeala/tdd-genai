import heapq

def nth_super_ugly_number(n, primes):
    ugly_numbers = [1]
    indices = [0] * len(primes)
    values = list(primes)
    
    for _ in range(1, n):
        next_ugly = min(values)
        ugly_numbers.append(next_ugly)
        
        for j in range(len(primes)):
            if values[j] == next_ugly:
                indices[j] += 1
                values[j] = ugly_numbers[indices[j]] * primes[j]
    
    return ugly_numbers[-1]
