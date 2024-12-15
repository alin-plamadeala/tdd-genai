import heapq

def cheap_items(items, n):
    heap = [(item['price'], item) for item in items]
    heapq.heapify(heap)
    result = []
    for _ in range(min(n, len(items))):
        price, item = heapq.heappop(heap)
        result.append(item)
    return result