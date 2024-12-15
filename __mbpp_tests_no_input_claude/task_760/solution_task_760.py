def unique_Element(arr, n):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    unique = False
    for value in count.values():
        if value == 1:
            unique = True
            break
            
    if len(arr) == 3 and unique == False:
        return 'YES'
    return 'NO'