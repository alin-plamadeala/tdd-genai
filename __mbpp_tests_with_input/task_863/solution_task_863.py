def find_longest_conseq_subseq(arr, n):
    if n == 0:
        return 0

    unique_elements = set(arr)
    longest_streak = 0

    for num in unique_elements:
        if num - 1 not in unique_elements:  # Start of a new sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in unique_elements:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
