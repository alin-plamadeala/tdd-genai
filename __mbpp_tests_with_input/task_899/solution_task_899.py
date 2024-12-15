def check(arr, n):
    left = 0
    right = len(arr) - 1
    last_picked = float('-inf')
    picked_count = 0

    while picked_count < n:
        if left > right:
            return False

        if arr[left] >= last_picked and (arr[right] < last_picked or arr[left] <= arr[right]):
            last_picked = arr[left]
            left += 1
        elif arr[right] >= last_picked:
            last_picked = arr[right]
            right -= 1
        else:
            return False

        picked_count += 1

    return True
