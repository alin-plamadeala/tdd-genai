from itertools import combinations

def find_triplet_array(arr, n, target_sum):
    for triplet in combinations(arr, 3):
        if sum(triplet) == target_sum:
            return triplet
    return None