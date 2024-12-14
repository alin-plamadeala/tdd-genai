# def remove_kth_element(lst, k):
#     current_count = {}
#     for i, elem in enumerate(lst):
#         if elem not in current_count:
#             current_count[elem] = 0
#         current_count[elem] += 1
#
#         if current_count[elem] == k:
#             return lst[:i] + lst[i+1:]
#
#     return lst


def remove_kth_element(lst, k):

    return lst[:k-1] + lst[k:]
