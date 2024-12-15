import re

def extract_date(url):
    # Use regex to extract the date in the format YYYY/MM/DD or YYYY-MM-DD from the URL
    pattern = r'(\d{4})[/-](\d{2})[/-](\d{2})'
    matches = re.findall(pattern, url)
    return matches
