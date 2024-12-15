import re

def extract_quotation(text):
    pattern = r'"([^"]*)"'
    matches = re.findall(pattern, text)
    return matches