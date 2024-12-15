from typing import List, Tuple

def re_arrange_tuples(input_list: List[Tuple[int, int]], order: List[int]) -> List[Tuple[int, int]]:
    # Create a mapping of the first element of each tuple to the tuple itself
    input_map = {}
    for tup in input_list:
        if tup[0] not in input_map:
            input_map[tup[0]] = []
        input_map[tup[0]].append(tup)

    # Build the result list based on the order
    result = []
    for value in order:
        if value in input_map and input_map[value]:
            result.append(input_map[value].pop(0))  # Use and remove the first tuple from the list
            input_map[value].append(result[-1])    # Re-add the tuple to allow reuse in case of duplicates

    return result
