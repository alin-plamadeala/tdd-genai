from typing import Tuple, Dict, Any

def add_dict_to_tuple(input_tuple: Tuple[Any, ...], input_dict: Dict[Any, Any]) -> Tuple[Any, ...]:
    return input_tuple + (input_dict,)