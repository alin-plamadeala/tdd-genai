def occurance_substring(main_string, substring):
    start_index = main_string.find(substring)
    if start_index == -1:
        return None
    end_index = start_index + len(substring)
    return (substring, start_index, end_index)