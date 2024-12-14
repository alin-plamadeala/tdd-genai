from typing import List
import re

def split_list(s: str) -> List[str]:
    return re.findall(r'[A-Z][a-z]*|[A-Z]+(?=[A-Z][a-z])|[A-Z]+|[^A-Za-z]+', s)