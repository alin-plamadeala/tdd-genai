def find_k_product(tuples_list, k):
    if k < 0 or k >= len(tuples_list[0]):
        raise ValueError("Invalid k value")

    product = 1
    for tpl in tuples_list:
        product *= tpl[k]
    return product
