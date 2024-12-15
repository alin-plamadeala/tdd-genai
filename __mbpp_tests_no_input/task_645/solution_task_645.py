def find_k_product(tuples_list, k):
    if not tuples_list or k < 0 or k >= len(tuples_list[0]):
        raise ValueError("Invalid input")

    product = 1
    for tpl in tuples_list:
        product *= tpl[k]

    return product
