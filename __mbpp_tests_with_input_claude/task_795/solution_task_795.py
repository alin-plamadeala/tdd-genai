import heapq

def cheap_items(items, n):
    heap = [(item['price'], item) for item in items]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(min(n, len(items)))]