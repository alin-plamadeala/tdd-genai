def length_Of_Last_Word(s: str) -> int:
    if not s.strip():  # Check for empty or whitespace-only strings
        return 0
    words = s.split()  # Split the string into words
    return len(words[-1])  # Return the length of the last word
