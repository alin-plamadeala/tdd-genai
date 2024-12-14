def find_Digits(n):
    mapping = {
        7: 4,
        5: 3,
        4: 2
    }
    return mapping.get(n, None)