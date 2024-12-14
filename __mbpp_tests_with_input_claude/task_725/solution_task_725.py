import re

def extract_quotation(string):
    pattern = r'"([^"]*)"'
    matches = re.findall(pattern, string)
    return matches