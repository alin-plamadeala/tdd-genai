import heapq

def heap_sort(iterable):
    if not isinstance(iterable, list):
        raise TypeError("Input must be a list")
    heap = []
    for value in iterable:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for _ in range(len(heap))]
