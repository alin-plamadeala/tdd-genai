def max_sum_subseq(arr):
    if not arr:
        return 0

    incl = 0
    excl = 0

    for num in arr:
        new_excl = max(incl, excl)
        incl = excl + num
        excl = new_excl

    return max(incl, excl)
