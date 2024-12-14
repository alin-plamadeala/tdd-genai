def occurance_substring(string, substring):
    start = string.find(substring)
    if start != -1:
        end = start + len(substring)
        return (substring, start, end)
    return None