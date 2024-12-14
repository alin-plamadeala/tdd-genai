def re_arrange_tuples(tuples_list, order_list):
    result = []
    
    for value in order_list:
        for tup in tuples_list:
            if tup[0] == value:
                result.append(tup)
                break
                
    return result