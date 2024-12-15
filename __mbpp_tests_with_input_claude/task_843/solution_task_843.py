def nth_super_ugly_number(n, primes):
    import heapq
    heap = [1]
    seen = {1}
    ugly = 1
    
    for _ in range(n):
        ugly = heapq.heappop(heap)
        for prime in primes:
            next_ugly = ugly * prime
            if next_ugly not in seen:
                seen.add(next_ugly)
                heapq.heappush(heap, next_ugly)
    
    return ugly