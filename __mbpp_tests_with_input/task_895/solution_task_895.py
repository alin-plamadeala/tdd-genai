def max_sum_subseq(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]

    prev_prev = 0
    prev = arr[0]

    for i in range(1, len(arr)):
        current = max(prev, prev_prev + arr[i])
        prev_prev = prev
        prev = current

    return prev
