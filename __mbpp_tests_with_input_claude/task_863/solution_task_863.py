def find_longest_conseq_subseq(nums, n):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            current_streak = 1
            
            while current + 1 in num_set:
                current += 1
                current_streak += 1
            
            longest = max(longest, current_streak)
    
    return longest