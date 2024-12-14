def min_Swaps(s1, s2):
    if len(s1) != len(s2):
        return -1

    swap_count = 0
    count_0_1 = 0
    count_1_0 = 0

    for char1, char2 in zip(s1, s2):
        if char1 == '0' and char2 == '1':
            count_0_1 += 1
        elif char1 == '1' and char2 == '0':
            count_1_0 += 1

    if (count_0_1 + count_1_0) % 2 != 0:
        return -1

    swap_count += count_0_1 // 2
    swap_count += count_1_0 // 2
    swap_count += (count_0_1 % 2) * 2

    return swap_count
