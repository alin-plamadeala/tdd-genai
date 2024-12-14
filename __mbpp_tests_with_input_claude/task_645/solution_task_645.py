def find_k_product(tuples, k):
    product = 1
    for tuple in tuples:
        product *= tuple[k]
    return product