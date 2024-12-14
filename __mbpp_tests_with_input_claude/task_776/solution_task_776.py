def count_vowels(s):
    vowels = set('aeiou')
    count = 0
    for i in range(len(s)):
        if s[i] not in vowels:
            if (i > 0 and s[i-1] in vowels) or (i < len(s)-1 and s[i+1] in vowels):
                count += 1
    return count