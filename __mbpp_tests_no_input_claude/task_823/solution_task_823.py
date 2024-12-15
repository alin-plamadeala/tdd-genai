def check_substring(text: str, substring: str) -> str:
    if text.startswith(substring):
        return 'string starts with the given substring'
    return 'string doesnt start with the given substring'