def find_k_product(tuples, k):
    product = 1
    for tuple_item in tuples:
        product *= tuple_item[k]
    return product