class Solution:
    def nth_super_ugly_number(self, n, primes):
        import heapq
        
        ugly_numbers = [1]
        heap = []
        for prime in primes:
            heapq.heappush(heap, (prime, prime, 0))
        
        while len(ugly_numbers) < n:
            next_ugly, prime, index = heapq.heappop(heap)
            
            if next_ugly != ugly_numbers[-1]:
                ugly_numbers.append(next_ugly)
            
            heapq.heappush(heap, (prime * ugly_numbers[index + 1], prime, index + 1))
        
        return ugly_numbers[-1]

def nth_super_ugly_number(n, primes):
    return Solution().nth_super_ugly_number(n, primes)