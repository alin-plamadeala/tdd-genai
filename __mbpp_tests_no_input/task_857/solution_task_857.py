from typing import List

def listify_list(input_list: List[str]) -> List[List[str]]:
    return [list(item) for item in input_list]