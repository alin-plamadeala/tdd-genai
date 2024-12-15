def min_Swaps(s1, s2):
    if len(s1) != len(s2):
        return "Not Possible"

    count_0_to_1 = 0
    count_1_to_0 = 0

    for bit1, bit2 in zip(s1, s2):
        if bit1 == '0' and bit2 == '1':
            count_0_to_1 += 1
        elif bit1 == '1' and bit2 == '0':
            count_1_to_0 += 1

    if count_0_to_1 != count_1_to_0:
        return "Not Possible"

    return count_0_to_1
