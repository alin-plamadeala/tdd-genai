def count_reverse_pairs(strings):
    count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if strings[i] == strings[j][::-1]:
                count += 1
    return str(count)