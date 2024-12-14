def check_str(s):
    if len(s) >= 5:
        return 'Valid' if s[0].islower() and s[-1].islower() else 'Invalid'
    else:
        return 'Valid' if s[0].isupper() else 'Invalid'