def rgb_to_hsv(r, g, b):
    r_scaled = r / 255.0
    g_scaled = g / 255.0
    b_scaled = b / 255.0

    max_val = max(r_scaled, g_scaled, b_scaled)
    min_val = min(r_scaled, g_scaled, b_scaled)
    delta = max_val - min_val

    if delta == 0:
        h = 0
    elif max_val == r_scaled:
        h = (60 * ((g_scaled - b_scaled) / delta) + 360) % 360
    elif max_val == g_scaled:
        h = (60 * ((b_scaled - r_scaled) / delta) + 120) % 360
    else:
        h = (60 * ((r_scaled - g_scaled) / delta) + 240) % 360

    s = 0 if max_val == 0 else (delta / max_val) * 100
    v = max_val * 100

    return (h, s, v)
