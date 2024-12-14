def find_Sum(arr, k):
    unique_elements = set()
    for num in arr:
        if arr.count(num) <= k:
            unique_elements.add(num)
    return sum(unique_elements)