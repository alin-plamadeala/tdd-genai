def extract_max(s):
    import re
    numbers = re.findall(r'\d+', s)
    if not numbers:
        raise ValueError("No numbers found in the input string")
    max_number = max(map(int, numbers))
    return max_number
