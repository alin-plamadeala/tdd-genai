def min_Num(arr, target):
    arr.sort(reverse=True)
    n = len(arr)
    min_count = float('inf')

    def backtrack(index, current_sum, count):
        nonlocal min_count
        # If the current sum meets or exceeds the target, update min_count
        if current_sum >= target:
            min_count = min(min_count, count)
            return
        # If we've reached the end of the array or the current count exceeds min_count, stop
        if index == n or count >= min_count:
            return

        # Include the current element
        backtrack(index + 1, current_sum + arr[index], count + 1)

        # Exclude the current element
        backtrack(index + 1, current_sum, count)

    backtrack(0, 0, 0)
    return min_count if min_count != float('inf') else -1
