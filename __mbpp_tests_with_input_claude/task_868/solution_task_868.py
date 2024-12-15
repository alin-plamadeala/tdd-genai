def length_Of_Last_Word(s: str) -> int:
    if not s:
        return 0
    return len(s.strip().split()[-1]) if s.strip() else 0