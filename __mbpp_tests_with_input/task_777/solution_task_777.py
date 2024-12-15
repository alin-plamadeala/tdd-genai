def find_Sum(arr, target):
    from collections import Counter
    element_counts = Counter(arr)
    return sum(num * count for num, count in element_counts.items() if count == target)
