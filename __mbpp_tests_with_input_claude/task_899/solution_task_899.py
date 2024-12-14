def check(arr, n):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] <= arr[right]:
            left += 1
        elif arr[right] <= arr[left]:
            right -= 1
        else:
            return False

    return True
