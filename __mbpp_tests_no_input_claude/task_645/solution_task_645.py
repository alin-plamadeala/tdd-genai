def find_k_product(tuples, k):
    product = 1
    for t in tuples:
        product *= t[k]
    return product