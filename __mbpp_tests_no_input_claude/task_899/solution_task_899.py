def check(nums, n):
    if len(nums) != n:
        return False
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and abs(i - j) >= 2:
                return True
                
    return False