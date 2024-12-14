def occurance_substring(main_string, substring):
    start = main_string.find(substring)
    if start != -1:
        end = start + len(substring)
        return (substring, start, end)
    return None