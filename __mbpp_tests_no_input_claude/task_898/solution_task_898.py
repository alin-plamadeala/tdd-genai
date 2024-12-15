def extract_elements(arr, n):
    result = []
    for num in set(arr):
        if arr.count(num) >= n:
            result.append(num)
    return sorted(result)