import heapq

def maximum_product(nums):
    if len(nums) < 3:
        raise ValueError("Input array must have at least three numbers")

    # Find the three largest numbers
    largest = heapq.nlargest(3, nums)
    # Find the two smallest numbers
    smallest = heapq.nsmallest(2, nums)

    # Calculate the maximum product
    return max(largest[0] * largest[1] * largest[2], smallest[0] * smallest[1] * largest[0])
