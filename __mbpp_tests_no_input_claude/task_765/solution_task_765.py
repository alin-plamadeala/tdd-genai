def is_polite(n):
    def is_polite_number(x):
        for start in range(1, x):
            sum_seq = 0
            for j in range(start, x+1):
                sum_seq += j
                if sum_seq == x and j > start:
                    return True
                if sum_seq > x:
                    break
        return False
    
    next_num = n + 1
    while not is_polite_number(next_num):
        next_num += 1
    return next_num