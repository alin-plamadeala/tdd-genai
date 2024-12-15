def replace(text, char):
    if len(text) <= 1:
        return text
    
    first_occurrence = text.find(char)
    if first_occurrence == -1:
        return text
        
    return text[:first_occurrence] + text[first_occurrence + 1:]