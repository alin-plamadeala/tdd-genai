def max_product(lst):
    n = len(lst)
    max_pair = (lst[0], lst[1])
    max_prod = lst[0] * lst[1]
    
    for i in range(n):
        for j in range(i + 1, n):
            curr_prod = lst[i] * lst[j]
            if curr_prod > max_prod:
                max_prod = curr_prod
                max_pair = (lst[i], lst[j])
    
    return max_pair