def min_Swaps(s1, s2):
    # Check if the lengths of the strings are the same
    if len(s1) != len(s2):
        return "Not Possible"

    # Count the number of mismatched 0s and 1s
    mismatched_01 = 0  # s1 has 0, s2 has 1
    mismatched_10 = 0  # s1 has 1, s2 has 0

    for char1, char2 in zip(s1, s2):
        if char1 == '0' and char2 == '1':
            mismatched_01 += 1
        elif char1 == '1' and char2 == '0':
            mismatched_10 += 1

    # If the total mismatches of 0->1 and 1->0 are not equal, it's not possible
    if (mismatched_01 + mismatched_10) % 2 != 0:
        return "Not Possible"

    # The minimum swaps required is the maximum of mismatched_01 and mismatched_10
    return max(mismatched_01, mismatched_10)
