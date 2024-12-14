def check(s):
    vowels = set('aeiou')
    s_lower = s.lower()
    return 'accepted' if vowels.issubset(s_lower) else 'not accepted'
