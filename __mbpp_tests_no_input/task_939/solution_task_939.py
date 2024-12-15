from typing import List, Dict

def sorted_models(models: List[Dict[str, str]]) -> List[Dict[str, str]]:
    return sorted(models, key=lambda x: (-x['model'], x['make'].lower()))