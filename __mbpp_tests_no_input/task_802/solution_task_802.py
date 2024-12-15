def count_Rotation(arr, n):
    low, high = 0, n - 1

    # Check if the array is sorted in descending order
    if arr[0] > arr[-1]:
        return (arr.index(max(arr)) + 1) % n

    while low <= high:
        if arr[low] <= arr[high]:
            return low

        mid = (low + high) // 2
        next_index = (mid + 1) % n
        prev_index = (mid - 1 + n) % n

        if arr[mid] <= arr[next_index] and arr[mid] <= arr[prev_index]:
            return mid

        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1

    return -1