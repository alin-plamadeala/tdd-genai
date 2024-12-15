def heap_sort(arr):
    heap = []
    for value in arr:
        heapify_up(heap, value)
    
    result = []
    while heap:
        result.append(pop_min(heap))
    return result

def heapify_up(heap, value):
    heap.append(value)
    current = len(heap) - 1
    
    while current > 0:
        parent = (current - 1) // 2
        if heap[parent] > heap[current]:
            heap[parent], heap[current] = heap[current], heap[parent]
            current = parent
        else:
            break

def pop_min(heap):
    if not heap:
        return None
    
    min_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    
    if heap:
        current = 0
        while True:
            smallest = current
            left = 2 * current + 1
            right = 2 * current + 2
            
            if left < len(heap) and heap[left] < heap[smallest]:
                smallest = left
            if right < len(heap) and heap[right] < heap[smallest]:
                smallest = right
                
            if smallest == current:
                break
                
            heap[current], heap[smallest] = heap[smallest], heap[current]
            current = smallest
            
    return min_val