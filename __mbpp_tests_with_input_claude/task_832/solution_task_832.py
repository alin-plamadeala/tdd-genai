import re

def extract_max(s):
    numbers = re.findall(r'\d+', s)
    return max(map(int, numbers))