def sum_in_Range(start: int, end: int) -> int:
    if start == end:
        return start
    elif end - start == 1:
        return start + end
    elif end - start == 2:
        return start + (start + 1) + end
    else:
        return start + (start + 1) + end - 2