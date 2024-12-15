def find_platform(arrivals, departures, n):
    arrivals.sort()
    departures.sort()

    platform_needed = 1
    max_platforms = 1

    i = 1
    j = 0

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platform_needed += 1
            i += 1
        elif arrivals[i] > departures[j]:
            platform_needed -= 1
            j += 1

        max_platforms = max(max_platforms, platform_needed)

    return max_platforms
