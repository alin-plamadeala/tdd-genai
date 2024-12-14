def check_min_heap(arr, i):
    n = len(arr)
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] > arr[left]:
        return False

    if right < n and arr[i] > arr[right]:
        return False

    if left < n and not check_min_heap(arr, left):
        return False

    if right < n and not check_min_heap(arr, right):
        return False

    return True