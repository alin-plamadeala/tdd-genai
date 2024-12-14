def are_Rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = str1 + str1
    if str2 in temp:
        return True
    return False