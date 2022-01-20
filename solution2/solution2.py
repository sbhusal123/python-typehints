from typing import List, Dict, Iterator, Tuple, Iterable

from itertools import groupby

def group_names(names: List[str]) -> Dict[int, list]:
    group_iter: Iterator[Tuple[int, Iterable[str]]]  = groupby(sorted(names,key=len), lambda x: len(x))
    return {k: list(v) for k, v in group_iter}
