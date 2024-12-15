def find_k_product(tuples_list, k):
    product = 1
    for tpl in tuples_list:
        if k < len(tpl):
            product *= tpl[k]
        else:
            raise IndexError("Index k is out of bounds for one of the tuples.")
    return product
