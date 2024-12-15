def check_tuples(input_tuple, elements_list):
    if len(input_tuple) != len(elements_list) * 2:
        return False
    
    for element in elements_list:
        if input_tuple.count(element) != 2:
            return False
    
    return True
