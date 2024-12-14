import heapq

def maximum_product(nums):
    if len(nums) < 3:
        return None
    
    largest = heapq.nlargest(3, nums)
    smallest = heapq.nsmallest(2, nums)
    
    return max(largest[0] * largest[1] * largest[2],
               largest[0] * smallest[0] * smallest[1])