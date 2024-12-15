def re_arrange_tuples(tuples_list, order_list):
    from collections import defaultdict

    # Create a dictionary to hold lists of tuples for each key in tuples_list
    tuple_dict = defaultdict(list)
    for t in tuples_list:
        tuple_dict[t[0]].append(t)

    # Result list to store the rearranged tuples
    result = []

    # Iterate over the order_list and append tuples in the correct order
    for key in order_list:
        if key in tuple_dict and tuple_dict[key]:
            result.append(tuple_dict[key][0])  # Append the first tuple for the key
        else:
            # If the key is repeated and no tuples are left, reuse the last tuple for the key
            if key in tuple_dict:
                result.append(tuple_dict[key][-1])

    return result
