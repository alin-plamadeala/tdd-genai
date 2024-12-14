def get_ludic(n):
    ludic = [1]
    candidates = list(range(2, n + 1))
    while candidates:
        next_ludic = candidates[0]
        if next_ludic > n:
            break
        ludic.append(next_ludic)
        candidates = [candidates[i] for i in range(len(candidates)) if (i + 1) % next_ludic != 0]
    return ludic