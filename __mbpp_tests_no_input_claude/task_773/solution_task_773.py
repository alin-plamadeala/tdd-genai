def occurance_substring(text, substring):
    start = text.find(substring)
    end = start + len(substring)
    return (substring, start, end)