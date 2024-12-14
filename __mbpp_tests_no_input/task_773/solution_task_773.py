def occurance_substring(text, substring):
    start_index = text.find(substring)
    if start_index == -1:
        return None
    end_index = start_index + len(substring)
    return (substring, start_index, end_index)
