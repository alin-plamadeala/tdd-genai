def is_Isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False

    mapping_s1_to_s2 = {}
    mapping_s2_to_s1 = {}

    for char1, char2 in zip(s1, s2):
        if char1 in mapping_s1_to_s2:
            if mapping_s1_to_s2[char1] != char2:
                return False
        else:
            mapping_s1_to_s2[char1] = char2

        if char2 in mapping_s2_to_s1:
            if mapping_s2_to_s1[char2] != char1:
                return False
        else:
            mapping_s2_to_s1[char2] = char1

    return True
