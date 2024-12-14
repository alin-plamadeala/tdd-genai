def extract_quotation(text):
    import re
    return re.findall(r'"(.*?)"', text)