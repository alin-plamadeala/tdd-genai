def sort_tuple(input_list):
    def sort_key(item):
        if isinstance(item[1], int):
            return (item[0], item[1])
        else:
            return (item[0], float('inf'))
    
    return sorted(input_list, key=sort_key)
