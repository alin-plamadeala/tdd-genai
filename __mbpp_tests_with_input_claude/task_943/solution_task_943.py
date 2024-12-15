import heapq

def combine_lists(list1, list2):
    heap = []
    result = []
    
    for num in list1:
        heapq.heappush(heap, (num, 1))
    for num in list2:
        heapq.heappush(heap, (num, 2))
        
    while heap:
        num, source = heapq.heappop(heap)
        result.append(num)
        
    return result