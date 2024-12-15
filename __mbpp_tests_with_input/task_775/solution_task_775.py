def odd_position(lst):
    for i in range(1, len(lst), 2):  # Iterate over odd indices
        if lst[i] % 2 == 0:  # Check if the number at the odd index is even
            return False
    return True
