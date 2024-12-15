def rearrange_numbs(nums):
    positive_sorted = sorted([num for num in nums if num > 0])
    negative_sorted = sorted([num for num in nums if num < 0], reverse=True)
    return positive_sorted + negative_sorted
