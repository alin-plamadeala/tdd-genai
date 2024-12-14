def min_Num(lst, n):
    sorted_lst = sorted(lst)
    return sorted_lst[n - 1] if 1 <= n <= len(sorted_lst) else None
