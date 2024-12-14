def length_Of_Last_Word(s):
    words = s.strip().split()
    return len(words[-1]) if words else 0