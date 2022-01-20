from typing import Dict, List, Union

# List[Union[str, int]]

def group_names(names: list) -> Dict[int, List[str]]:
    """General implementation by iterating over list"""
    grouped: Dict[int, List[str]] = {}
    for name in names:
        length: int = len(name)
        try:
           grouped[length].append(name)
        except KeyError: # KeyError raised if key is not found
            grouped[length] = [name]
    return grouped