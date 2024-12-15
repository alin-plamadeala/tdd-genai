def find_longest_conseq_subseq(arr, n):
    if not arr or n == 0:
        return 0

    arr = set(arr)
    longest_streak = 0

    for num in arr:
        if num - 1 not in arr:
            current_num = num
            current_streak = 1

            while current_num + 1 in arr:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
