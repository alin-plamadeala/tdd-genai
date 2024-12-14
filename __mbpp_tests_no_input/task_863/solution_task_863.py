def find_longest_conseq_subseq(arr, n):
    if n == 0:
        return 0
    
    arr = list(set(arr))
    arr.sort()
    
    longest_streak = 1
    current_streak = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1
    
    longest_streak = max(longest_streak, current_streak)
    
    return longest_streak
