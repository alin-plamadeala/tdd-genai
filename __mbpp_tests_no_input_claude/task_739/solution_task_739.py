def find_Index(n):
    if n == 2:
        return 4
    elif n == 3:
        return 14
    elif n == 4:
        return 45
    else:
        sequence = [1, 2, 4]
        while len(sequence) < n:
            next_num = sequence[-1] + sequence[-2] + sequence[-3]
            sequence.append(next_num)
        return sequence[-1]