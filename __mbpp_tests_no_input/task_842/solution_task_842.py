from collections import Counter

def get_odd_occurence(arr, n):
    count = Counter(arr)
    for num in count:
        if count[num] % 2 != 0:
            return num
    return None