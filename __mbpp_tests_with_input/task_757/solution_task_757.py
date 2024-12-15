def count_reverse_pairs(string_list):
    reverse_pairs_count = 0
    seen = set()
    
    for string in string_list:
        reversed_string = string[::-1]
        if reversed_string in seen:
            reverse_pairs_count += 1
        seen.add(string)
    
    return str(reverse_pairs_count)
