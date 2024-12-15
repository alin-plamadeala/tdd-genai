def remove_length(text: str, length: int) -> str:
    words = text.split()
    filtered_words = [word for word in words if len(word) != length]
    return ' '.join(filtered_words)