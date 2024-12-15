def check(arr, n):
    def can_make_sorted(left, right, prev, count):
        if count == n:
            return True
        if left > right:
            return False
            
        if arr[left] >= prev:
            if can_make_sorted(left + 1, right, arr[left], count + 1):
                return True
                
        if arr[right] >= prev:
            if can_make_sorted(left, right - 1, arr[right], count + 1):
                return True
                
        return False

    return can_make_sorted(0, len(arr)-1, float('-inf'), 0)