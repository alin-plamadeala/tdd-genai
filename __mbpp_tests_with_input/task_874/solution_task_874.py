def check_Concat(s, sub):
    if not sub:  # Handle edge case where sub is an empty string
        return False
    if len(s) % len(sub) != 0:  # If s is not a multiple of sub's length, it can't be a concatenation
        return False
    repeated = sub * (len(s) // len(sub))  # Repeat sub to match the length of s
    return repeated == s
