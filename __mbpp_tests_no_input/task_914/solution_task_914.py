def is_Two_Alter(s):
    if len(s) < 2:
        return False

    char1 = s[0]
    char2 = None

    for i in range(1, len(s)):
        if s[i] == char1:
            if i % 2 == 0:
                continue
            else:
                return False
        elif char2 is None:
            char2 = s[i]
            if i % 2 == 1:
                continue
            else:
                return False
        elif s[i] == char2:
            if i % 2 == 1:
                continue
            else:
                return False
        else:
            return False

    return True
