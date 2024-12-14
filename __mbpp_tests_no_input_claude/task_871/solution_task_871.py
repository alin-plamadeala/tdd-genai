def are_Rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    return str1 in (str2 + str2)