def count_duplic(arr):
    nums = []
    counts = []
    count_dict = {}
    
    for num in arr:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    
    seen = set()
    for num in arr:
        if num not in seen:
            nums.append(num)
            counts.append(count_dict[num])
            seen.add(num)
            
    return nums, counts