def re_arrange_tuples(tuples_list, order_list):
    order_dict = {}
    order_index = 0
    result = []
    
    for value in order_list:
        for tup in tuples_list:
            if tup[0] == value:
                result.append(tup)
                order_dict[value] = order_index
                order_index += 1
                break
    
    return result
