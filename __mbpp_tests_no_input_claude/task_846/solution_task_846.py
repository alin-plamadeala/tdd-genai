def find_platform(arrivals, departures, n):
    arrivals.sort()
    departures.sort()

    platform_needed = 1
    result = 1
    i = 1
    j = 0

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platform_needed += 1
            i += 1
            if platform_needed > result:
                result = platform_needed
        else:
            platform_needed -= 1
            j += 1

    return result
