def rearrange_numbs(nums):
    positive_nums = sorted([num for num in nums if num >= 0])
    negative_nums = sorted([num for num in nums if num < 0])
    return positive_nums + negative_nums
