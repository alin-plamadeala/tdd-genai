def extract_elements(arr, n):
    return list(set([x for x in arr if arr.count(x) >= n]))