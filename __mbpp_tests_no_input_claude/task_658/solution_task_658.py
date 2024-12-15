def max_occurrences(arr):
    count_dict = {}
    max_count = 0
    max_num = None
    
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
        if count_dict[num] > max_count:
            max_count = count_dict[num]
            max_num = num
        elif count_dict[num] == max_count:
            max_num = min(max_num, num)
            
    return max_num