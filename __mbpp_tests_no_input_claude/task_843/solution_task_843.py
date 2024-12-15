def nth_super_ugly_number(n, primes):
    ugly = [1]
    indices = [0] * len(primes)
    next_multiples = primes.copy()
    
    for _ in range(1, n):
        next_ugly = min(next_multiples)
        ugly.append(next_ugly)
        
        for i in range(len(primes)):
            if next_ugly == next_multiples[i]:
                indices[i] += 1
                next_multiples[i] = ugly[indices[i]] * primes[i]
    
    return ugly[-1]