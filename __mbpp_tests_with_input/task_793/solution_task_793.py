def last(arr, element, n):
    left, right = 0, n - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == element:
            result = mid
            left = mid + 1
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return result
