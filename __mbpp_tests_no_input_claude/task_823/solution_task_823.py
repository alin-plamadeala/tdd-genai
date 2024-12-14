def check_substring(main_string, substring):
    if main_string.startswith(substring):
        return 'string starts with the given substring'
    else:
        return 'string doesnt start with the given substring'