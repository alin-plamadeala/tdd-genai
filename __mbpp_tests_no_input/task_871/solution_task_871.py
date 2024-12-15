def are_Rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    combined = str1 + str1
    return str2 in combined
