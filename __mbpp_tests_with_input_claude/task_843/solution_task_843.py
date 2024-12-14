import heapq

def nth_super_ugly_number(n, primes):
    ugly = [1]
    heap = [(p, p, 0) for p in primes]
    heapq.heapify(heap)

    while len(ugly) < n:
        next_ugly, prime, index = heapq.heappop(heap)
        if next_ugly != ugly[-1]:
            ugly.append(next_ugly)
        heapq.heappush(heap, (prime * ugly[index + 1], prime, index + 1))

    return ugly[-1]