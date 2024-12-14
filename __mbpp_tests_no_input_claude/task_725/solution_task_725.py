def extract_quotation(text):
    result = []
    in_quote = False
    current_quote = ""
    for char in text:
        if char == '"':
            if in_quote:
                result.append(current_quote)
                current_quote = ""
            in_quote = not in_quote
        elif in_quote:
            current_quote += char
    return result