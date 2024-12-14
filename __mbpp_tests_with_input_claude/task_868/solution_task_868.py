def length_Of_Last_Word(s):
    s = s.strip()
    if not s:
        return 0
    return len(s.split()[-1])