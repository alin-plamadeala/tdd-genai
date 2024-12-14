def check_min_heap(heap, index):
    size = len(heap)
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and heap[index] > heap[left]:
        return False

    if right < size and heap[index] > heap[right]:
        return False

    if left < size and not check_min_heap(heap, left):
        return False

    if right < size and not check_min_heap(heap, right):
        return False

    return True