import re

def extract_date(url):
    # Regular expression to match the date pattern in the URL
    date_pattern = r'/(\d{4})/(\d{2})/(\d{2})/'
    match = re.search(date_pattern, url)
    if match:
        return [(match.group(1), match.group(2), match.group(3))]
    return []
