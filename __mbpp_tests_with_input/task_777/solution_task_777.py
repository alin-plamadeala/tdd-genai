def find_Sum(arr, n):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    return sum(unique_elements[:n])