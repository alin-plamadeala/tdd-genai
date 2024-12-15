import heapq

def heap_sort(arr):
    heap = []
    for value in arr:
        heapq.heappush(heap, value)
    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
    return sorted_arr
