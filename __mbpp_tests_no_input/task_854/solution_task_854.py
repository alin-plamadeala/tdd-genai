import heapq

def raw_heap(arr):
    heapq.heapify(arr)
    return list(arr)
