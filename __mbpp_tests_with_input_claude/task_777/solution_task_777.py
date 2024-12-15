def find_Sum(arr, n):
    unique_elements = set()
    for num in arr:
        unique_elements.add(num)
    return sum(unique_elements)