import re

def extract_max(s):
    numbers = re.findall(r'\d+', s)
    max_number = max(map(int, numbers))
    return max_number