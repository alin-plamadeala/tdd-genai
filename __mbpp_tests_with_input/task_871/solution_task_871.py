def are_Rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    return str2 in (str1 + str1)
