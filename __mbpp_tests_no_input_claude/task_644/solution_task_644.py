def reverse_Array_Upto_K(arr, k):
    if not arr or k <= 0:
        return arr
    k = min(k, len(arr))
    left = 0
    right = k - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr