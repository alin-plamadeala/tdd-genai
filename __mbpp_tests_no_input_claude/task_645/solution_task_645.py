def find_k_product(tuples, k):
    sorted_tuples = sorted(tuples, key=lambda x: x[k], reverse=True)
    return sorted_tuples[0][0] * sorted_tuples[0][1] * sorted_tuples[0][2]