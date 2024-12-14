def count_range_in_list(lst, start, end):
    if isinstance(start, str) and isinstance(end, str):
        start_index = lst.index(start) if start in lst else 0
        end_index = lst.index(end) if end in lst else len(lst)
        return end_index - start_index + 1
    else:
        return sum(1 for item in lst if start <= item <= end)