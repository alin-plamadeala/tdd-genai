def min_Swaps(s1, s2):
    if len(s1) != len(s2):
        return "Not Possible"

    x_diff = 0
    y_diff = 0

    for i in range(len(s1)):
        if s1[i] == '1' and s2[i] == '0':
            x_diff += 1
        elif s1[i] == '0' and s2[i] == '1':
            y_diff += 1

    if (x_diff + y_diff) % 2 != 0:
        return "Not Possible"

    return (x_diff // 2) + (y_diff // 2) + (x_diff % 2)