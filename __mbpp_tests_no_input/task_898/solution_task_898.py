class SolutionError(Exception):
    pass

def extract_elements(lst, n):
    if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
        raise SolutionError("Input must be a list of integers.")
    if not isinstance(n, int):
        raise SolutionError("n must be an integer.")
    if n <= 0:
        raise SolutionError("n must be a positive integer.")
    
    from collections import Counter
    counter = Counter(lst)
    result = [key for key, count in counter.items() if count == n]
    return sorted(result)