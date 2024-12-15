def average_tuple(nums):
    return [sum(x)/len(nums) for x in zip(*nums)]