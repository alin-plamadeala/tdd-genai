def is_polite(n):
    polite = []
    num = 1
    
    while len(polite) < n:
        is_current_polite = False
        for start in range(1, num):
            sum_seq = start
            next_num = start + 1
            while sum_seq <= num:
                if sum_seq == num and next_num - start >= 2:
                    is_current_polite = True
                    break
                sum_seq += next_num
                next_num += 1
                
        if is_current_polite:
            polite.append(num)
            
        num += 1
        
    return polite[n-1]