import re

def move_num(s):
    letters = re.sub(r'\d+', '', s)
    numbers = ''.join(re.findall(r'\d+', s))
    return letters + numbers
