from collections import Callable, Iterable
from typing import TypeVar, Dict, List

U = TypeVar('U')
R = TypeVar('R')


def groupby(f: Callable[[U], R], xs: Iterable[U]) -> Dict[R, List[U]]:
    r = dict()
    for x in xs:
        k = f(x)
        if k not in r:
            r[k] = []
        r[k].append(x)
    return r
