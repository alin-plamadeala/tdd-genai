def cheap_items(items, n):
    sorted_items = sorted(items, key=lambda x: x['price'])
    return sorted_items[:n]